import sqlalchemy
from .db_session import SqlAlchemyBase


class Films(SqlAlchemyBase):
    __tablename__ = 'films'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    films = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    genre = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    ratting = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    so_so = sqlalchemy.Column(sqlalchemy.String, nullable=False)