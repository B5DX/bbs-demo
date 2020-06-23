from module.model import Message, User, db
from datetime import datetime
from util import encryption
from sqlalchemy import func, or_


def get_time():
    now = datetime.now()
    return now.strftime('%Y-%m-%d  %H:%M:%S')


# didn't use
def check(content=None, username=None, time=None):
    """
    检查所给值是否符合表头数据类型和长度的要求
    :param content: content列内容，type=str, len < 511
    :param username: 留言人，type=str, len<20
    :param time: 留言时间，type=datetime, %Y-%m-%d %H:%M:%S, 使用datetime类，由getTime()获取
    :return: 无返回值，需要异常捕获
    """
    check_data = {
        'content': (str, 511),
        'username': (str, 20),
        'time': (str, 19)
    }
    values = [content, username, time]
    keys = list(check_data.keys())
    try:
        for ind, i in enumerate(values):
            if i is not None:
                tp = check_data[keys[ind]]
                # noinspection PyTypeHints
                assert isinstance(i, tp[0])
                assert len(i) <= tp[1]
    except Exception as e:
        print('invalid data.')
        raise e


def exception_handler(f):
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
        # 由于主键id默认了自增加，所以新建时为写id的值
        new_message = Message(content=content, username=username, time=get_time(), is_deleted=0)
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
        self.__session.close()


if __name__ == '__main__':
    for j in SQL.__dict__:
        print(j)
