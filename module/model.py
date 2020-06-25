from flask_login import UserMixin
from app import db, login
from util import encryption


class Message(db.Model):
    """
    A message class.
    """
    __tablename__ = 'message_board'

    id = db.Column(db.INTEGER(), primary_key=True)
    content = db.Column(db.String(511))
    username = db.Column(db.String(20))
    time = db.Column(db.DATETIME())


@login.user_loader
def load_user(user_id):
    """
    Used for flask_login.
    """
    return User.query.filter_by(user_id=user_id).first()


class User(UserMixin, db.Model):
    """
    Used for flask_login and SQL command.
    """
    __tablename__ = 'users'

    user_id = db.Column(db.INTEGER(), primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    register_date = db.Column(db.String())

    def __repr__(self):
        return f'<User: {self.username}>'

    def check_password(self, password):
        """
        Check if the password is correct for current user.
        :param password: unencrypted password
        :return:
        If the encrypted password for current user is the same as the password in database, return True.
        Else return False.
        """
        return self.password == encryption(password)

    def get_id(self):
        """
        Override the function in UserMixin.
        """
        return self.user_id
