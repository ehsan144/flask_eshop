from os import getenv as env
from dotenv import load_dotenv

from flask import Flask

from Catalog import CatalogResource
from Core import CoreResource
from .config import db, api

load_dotenv()

app = Flask(__name__)

# Configurations
app.config['SQLALCHEMY_DATABASE_URI'] = env("POSTGRESQL_URI")
app.config["SECRET_KEY"] = env("SECRET_KEY")

# add Resource

api.add_resource(CoreResource, "/")
api.add_resource(CatalogResource, "/catalog")

# Initial Libs

db.init_app(app)
api.init_app(app)
