from flask import jsonify, request
from flask_restful import Resource
from requests import get, post
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


class SendComment(Resource):
    """
    RESTFull
    """
    def post(self):
        """
        READ operation with DB for Employee table

        :return: employee list, 200 status code
        """
        if app.config['DB_LOCAL_COPY']:
            response = {
                        "id": "fcc9e1a3-6852-4141-9751-d8ecf27ce28c",
                        "app_id": 443810,
                        "nickname": "jholxpert",
                        "comment": "Yes",
                        "user_reaction": "joy"
                        }
        else:
            data = dict(request.form)
            headers = {'x-functions-key': app.config['DB_API_KEY_COMMENTS']}
            adress = app.config['RECORD_COMMENT']
            response = post(app.config['RECORD_COMMENT'],
                           headers=headers,
                           json=data)
            response = response.json()
        return response, 200