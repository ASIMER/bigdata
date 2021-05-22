from flask import request
from flask_restful import Resource
from requests import get
from BigDataProject import app

from BigDataProject.db_local_copy.db_local_data_loader import load_copy


class LoadGames(Resource):
    """
    RESTFull
    """
    def get(self):
        """
        READ operation with DB for Employee table

        :return: employee list, 200 status code
        """
        pagingState = request.args.get('pagingState')
        headers = {'x-functions-key': app.config['DB_API_KEY']}
        params = {'pagingState': pagingState}
        
        response = get(app.config['LIST_GAMES_WITH_PRICES'],
                       headers=headers,
                       params=params).json()
        return response, 200
