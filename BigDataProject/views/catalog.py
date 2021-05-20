from flask import Blueprint, redirect, render_template, url_for
from requests import get
from BigDataProject import app
from BigDataProject.db_local_copy.db_local_data_loader import load_copy

cart_routes = Blueprint('catalog', __name__)


@cart_routes.route('/', methods=['GET'])
def main() -> render_template:
    """
    main catalog page

    :return:
    """
    games = []
    if app.config['DB_LOCAL_COPY']:
        for page in load_copy():
            games += page['page']
    else:
        # load data from db
        headers = {'x-functions-key': app.config['DB_API_KEY']}
        response = get(app.config['LIST_GAMES_WITH_PRICES'],
                       headers=headers).json()
        pagingState, page = response['pagingState'], response['page']

    return render_template("main.html", games=games)


@cart_routes.route('/game_page/<string:name>', methods=['GET'])
def game_page(name) -> render_template:
    """
    main catalog page

    :return:
    """
    print("Name:", name)

    return redirect(url_for('catalog.main'))
