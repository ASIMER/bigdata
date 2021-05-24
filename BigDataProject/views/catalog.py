from datetime import datetime

from flask import Blueprint, redirect, render_template, url_for
from requests import get
from BigDataProject import app
from BigDataProject.db_local_copy.db_local_data_loader import load_copy

cart_routes = Blueprint('catalog', __name__, static_folder='static')


@cart_routes.route('/', methods=['GET'])
def main() -> render_template:
    """
    main catalog page

    :return:
    """
    games = []
    pagingState = None
    if app.config['DB_LOCAL_COPY']:
        for page in load_copy('BigDataProject/db_local_copy/db_local_data.txt'):
            games += page['page']
            pagingState = page['pagingState']
    else:
        # load data from db
        for page in range(2):
            headers = {'x-functions-key': app.config['DB_API_KEY']}
            params = {'pagingState': pagingState}
            response = get(app.config['LIST_GAMES_WITH_PRICES'],
                           headers=headers).json()
            pagingState = response['pagingState']
            games += response['page']
    return render_template("main.html", games=games, next_page=pagingState)


@cart_routes.route('/game_page/<name>', methods=['GET'])
def game_page(name, game_id = None) -> render_template:
    """
    main catalog page

    :return:
    """
    emotion_color = {
            "anger": "#DA6663",
            "fear": "#DA996B",
            "joy": "#BFB760",
            "love": "#ff75a7",
            "sadness": "#DA99B2",
            "surprise": "#5FBDDA",
            }
    print(app.config['DB_LOCAL_COPY'])
    if app.config['DB_LOCAL_COPY']:
        response = load_copy("BigDataProject/db_local_copy/db_local_data_game_info.txt")
        comments = load_copy("BigDataProject/db_local_copy/db_local_data_game_comments.txt")['comments']
    else:
        headers = {'x-functions-key': app.config['DB_API_KEY']}
        params = {'name': name}
        response = get(app.config['GET_GAME_BY_NAME'],
                       headers=headers,
                       params=params).json()

        comment_headers = {'x-functions-key': app.config['DB_API_KEY_COMMENTS']}
        comment_params = {'game_id': response['appId']}
        comments = get(app.config['GET_GAME_COMMENTS'],
                       headers=comment_headers,
                       params=comment_params).json()['comments']

    converted_data = [
            {"x": datetime.fromisoformat(record['datePrice']).timestamp() * 1000,
             "y": record['finalPrice']
             }
            for record in response['priceHistory']
            ]
    addition_data = []
    for i, day in enumerate(converted_data):
        if i > 0:
            part_day = day.copy()
            part_day['x'] = converted_data[i-1]['x'] + ( converted_data[i]['x'] - converted_data[i-1]['x']) / 4 * 2
            part_day['y'] = converted_data[i-1]['y'] + (converted_data[i]['y'] - converted_data[i-1]['y']) / 4 * 2
            addition_data.append(part_day)
            part_day = day.copy()
            part_day['x'] = converted_data[i-1]['x'] + ( converted_data[i]['x'] - converted_data[i-1]['x']) / 4 * 3
            part_day['y'] = converted_data[i-1]['y'] + (converted_data[i]['y'] - converted_data[i-1]['y']) / 4 * 3
            addition_data.append(part_day)
        addition_data.append(day)
    return render_template("dashboard.html",
                           data=addition_data,
                           game_info=response,
                           game_name=name,
                           game_id=game_id,
                           comments=comments,
                           emotion_color = emotion_color)
