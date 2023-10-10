from .base import BaseModel
from sqlalchemy import Column, String, Integer


class Product(BaseModel):
    __tablename__ = "products"
    title = Column(String(30))
    slug = Column(String(50), unique=True)
