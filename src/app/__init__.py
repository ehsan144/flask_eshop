from os import environ
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.db import db
from app.api import api

from app.Catalog import CatalogResource
from app.Core import CoreResource

app = Flask(__name__)

# Configurations

load_dotenv()
app.config.from_object(environ.get('APP_SETTINGS'))
# add Resource


api.add_resource(CoreResource, "/")
api.add_resource(CatalogResource, "/catalog")

# Initial Libs

db.init_app(app)
api.init_app(app)

# Initial DataBase

with app.app_context():
    db.create_all()
