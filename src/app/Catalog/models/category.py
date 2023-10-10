from sqlalchemy import Column, String

from .base import BaseModel


class Category(BaseModel):
    title = Column(String(30))
    slug = Column(String(50), unique=True)
