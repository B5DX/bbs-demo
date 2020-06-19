from module.model import Message, User, db
from datetime import datetime
from util import encryption
from typing import List


def get_time():
    now = datetime.now()
    return now.strftime('%Y-%m-%d %H:%M:%S')


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


def exception_handler(func):
    def res(*args):
        try:
            return func(*args)
        except Exception as e:
            print(f'{func.__name__} failed.')
            print(e)

    return res


class SQL:
    def __init__(self):
        self.__session = db.session

    @exception_handler
    def login(self, username, password) -> User:
        cmp = encryption(password)
        user: list[User] = self.__session.query(User).filter(User.username == username).all()
        if len(user) == 0:
            return None
        else:
            assert len(user) == 1
            if user[0].password == cmp:
                return user[0]
            else:
                return None

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

    @exception_handler
    def user_search(self, user_id) -> User:
        ls = self.__session.query(User).filter(User.user_id == user_id).all()
        if len(ls) == 0:
            return None
        else:
            return ls[0]

    def message_search(self, user_id=None, username=None) -> List[Message]:
        try:
            session = self.__session
            res = session.query(Message).filter(Message.is_deleted == 0)
            if isinstance(user_id, int):
                res = res.filter(Message.id == user_id).all()
            elif isinstance(username, str):
                res = res.filter(Message.username == username).all()
            else:
                res = res.all()
            return res
        except Exception:
            print('search failed.')
            return []

    @exception_handler
    def update(self, user_id, new_content, new_time):
        self.__session.query(Message).filter(Message.id == user_id).update({'content': new_content, 'time': new_time})
        self.__session.commit()

    @exception_handler
    def delete(self, user_id):
        self.__session.query(Message).filter(Message.id == user_id).update({'is_deleted': 1})
        self.__session.commit()

    @exception_handler
    def complete_delete(self, user_id=None):
        if not user_id:
            return
        session = self.__session
        session.query(Message).filter(Message.is_deleted == 1, Message.id == user_id).delete()
        session.commit()

    @exception_handler
    def clear_recycle_bin(self):
        session = self.__session
        session.query(Message).filter(Message.is_deleted == 1).delete()
        session.commit()

    @exception_handler
    def close(self):
        self.__session.close()


if __name__ == '__main__':
    # try:
    #     sql = SQL()
    #     sql.insert('test', '小明', get_time())
    #     sql.delete(10)
    #     sql.update(1, 'changed', get_time())
    #     for msg in sql.search(username='wzx'):
    #         msg: Message
    #         print(msg.content)
    #     sql.close()
    # except Exception:
    #     exit(0)
    for j in SQL.__dict__:
        print(j)
