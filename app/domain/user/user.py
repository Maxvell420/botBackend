from ...core.database.base import Base
from sqlalchemy import Column, Integer, String, JSON


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String)
