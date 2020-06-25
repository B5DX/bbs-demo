from module.model import Message, User, db
from datetime import datetime
from util import encryption
from sqlalchemy import func, or_


def get_time():
    """
    get current time
    :return: a str format by '%Y-%m-%d  %H:%M:%S'
    """
    now = datetime.now()
    return now.strftime('%Y-%m-%d  %H:%M:%S')


def exception_handler(f):
    """
    a decorator to handle exception
    :param f: a function to be decorated
    :return: a inner function which add try-except before run f
    """
    def res(*args):
        try:
            return f(*args)
        except Exception as e:
            print(f'{f.__name__} failed.')
            print(e)

    return res


class SQL:
    def __init__(self):
        self.__session = db.session

    @exception_handler
    def register(self, username, password) -> bool:
        """
        register a user. the parameter here is guaranteed valid.
        :return:
        True if successfully registered.
        if the username already exists, return False.
        """
        res = self.__session.query(User).filter(User.username == username).all()
        if len(res) == 0:
            cmp = encryption(password)
            new_user = User(username=username, password=cmp, register_date=get_time())
            self.__session.add(new_user)
            self.__session.commit()
            return True
        else:
            return False

    @exception_handler
    def insert_message(self, content, username):
        new_message = Message(content=content, username=username, time=get_time())
        self.__session.add(new_message)
        self.__session.commit()

    @staticmethod
    def search_message(keyword):
        result = Message.query.filter(
            or_(Message.content.contains(keyword), Message.username.contains(keyword))
        ).order_by(Message.time.desc()).all()
        return result

    def get_message_length(self):
        """
        get the number of all messages, which is used to decide the page number on index.html
        :return: the number of all messages
        """
        return self.__session.query(func.count(Message.id)).scalar()

    @exception_handler
    def update_message(self, message_id, new_content):
        """
        update an exist message.
        """
        self.__session.query(Message).filter(Message.id == message_id).\
            update({'content': new_content, 'time': get_time()})
        self.__session.commit()

    @exception_handler
    def delete_message(self, message_id):
        self.__session.query(Message).filter(Message.id == message_id).delete()
        self.__session.commit()

    @exception_handler
    def change_password(self, user_id, new_password):
        self.__session.query(User).filter(User.user_id == user_id).update({'password': encryption(new_password)})
        self.__session.commit()

    @exception_handler
    def close(self):
        """
        close session
        """
        self.__session.close()


if __name__ == '__main__':
    for j in SQL.__dict__:
        print(j)
