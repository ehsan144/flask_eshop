from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

db = SQLAlchemy()

# class BaseModel(db.Model):
#     id = Column(Integer, unique=True, primary_key=True, autoincrement=True)
