from os import environ
from dotenv import load_dotenv

from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate

from app.db import db
from app.Catalog.routes import CatalogResource
from app.Core.routes import CoreResource
from app.Catalog import models

app = Flask(__name__)
api = Api(app)

# Configurations

load_dotenv()
app.config.from_object(environ.get('APP_SETTINGS'))

# Initial Libs
db.init_app(app)
migrate = Migrate(app, db)

# add Resource


api.add_resource(CoreResource, "/")
api.add_resource(CatalogResource, "/catalog")

# Initial DataBase

with app.app_context():
    db.create_all()
