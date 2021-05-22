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
    print(pagingState)
    return render_template("main.html", games=games, next_page=pagingState)


@cart_routes.route('/game_page/<name>/<game_id>', methods=['GET'])
def game_page(name, game_id) -> render_template:
    """
    main catalog page

    :return:
    """
    headers = {'x-functions-key': app.config['DB_API_KEY']}
    params = {'gameName': name}
    print("headers", headers)
    print("params", params)
    print("GET_PRICE_OF_SPECIFIC_GAME", app.config['GET_PRICE_OF_SPECIFIC_GAME'])
    response = get(app.config['GET_PRICE_OF_SPECIFIC_GAME'],
                   headers=headers,
                   params=params)
    print("response", response)
    response = response.json()
    print("response", response)
    converted_data = [
            {"x": datetime.fromisoformat(record['datePrice']).timestamp() * 1000,
             "y": record['finalPrice']
             }
            for record in response
            ]

    return render_template("dashboard.html",
                           data=converted_data,
                           game_name=name,
                           game_id=game_id)
