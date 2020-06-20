import os


class Config:
    DIALECT = 'mysql'
    DRIVER = 'pymysql'
    USERNAME = 'root'
    PASSWORD = 'wrwzx'
    HOST = '127.0.0.1'
    PORT = '3306'
    DATABASE = 'message_board_db'

    # 'mysql+pymysql://root:'+password+'@localhost/test'
    SQLALCHEMY_DATABASE_URI = f'{DIALECT}+{DRIVER}://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}'

    POOL_SIZE = 5

    MAX_OVERFLOW = 10

    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # 用户登录需要用
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # 分页展示的设置
    POSTS_PER_PAGE = 11
