from flask_sqlalchemy import SQLAlchemy
from config import app
db = SQLAlchemy(app)


class Message(db.Model):
    # 表名
    __tablename__ = 'message_board'

    id = db.Column(db.INTEGER(), primary_key=True)
    content = db.Column(db.String(511))
    nickname = db.Column(db.String(20))
    time = db.Column(db.DATETIME())
    is_deleted = db.Column(db.INTEGER())


class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.INTEGER(), primary_key=True)
    nickname = db.Column(db.String(255))
    password = db.Column(db.String(255))
    register_date = db.Column(db.String())
