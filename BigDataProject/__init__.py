from os import fspath

from flask import Flask
from .config import Config
from flask_restful import Api
"""from flask_migrate import Migrate



from .middleware import Middleware
from .models import db"""

app = Flask(__name__, static_folder='static')
app.config.from_object(Config())
#app.wsgi_app = Middleware(app.wsgi_app)
api = Api(app)

from BigDataProject.rest.catalog import LoadGames, SendComment
api.add_resource(LoadGames, "/load_games")
api.add_resource(SendComment, "/send_comment")

import BigDataProject.views.catalog
app.register_blueprint(BigDataProject.views.catalog.cart_routes, static_folder='static', static_url_path='/static')

