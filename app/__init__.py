from os import getenv as env
from dotenv import load_dotenv

from flask import Flask
from Config import db, api
from Catalog import CatalogResource

load_dotenv()

app = Flask(__name__)

# Configurations
app.config['SQLALCHEMY_DATABASE_URI'] = env("POSTGRESQL_URI")
app.config["SECRET_KEY"] = env("SECRET_KEY")

# Initial Libs
db.init_app(app)
api.init_app(app)

# add Resource

api.add_resource(CatalogResource, "/catalog")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
