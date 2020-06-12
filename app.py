from config import app
from flask import url_for, request, redirect, render_template
from util import get_encrypted_code
from module import SQL, User
sql = SQL()


@app.route('/')
def root():
    """
    redirect to '/login'
    """
    return redirect('/login')


# finished
@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    page for signing in.
    :return:
    if sign in successfully, redirect to a url for certain user
    else return templates 'sign.html'
    """
    if request.method == 'POST':
        nickname = request.form['nickname']
        password = request.form['password']
        res = sql.login(nickname, password)
        if res is not None:
            return redirect(
                url_for('show_table', encrypted_code=get_encrypted_code(res.password[:10]), user_id=res.user_id)
            )
        else:
            return render_template('login.html', note='用户名或密码错误')
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', note='请登录')


# finished
@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    page for register
    :return:
    if register successfully, redirect to '/sign'
    else, return templates 'register.html'
    """
    if request.method == 'POST':
        # register
        nickname = request.form['nickname']
        password = request.form['password']
        # front side has checked the data, so the data here must be type valid.(maybe sql invalid, such as rename)
        if sql.register(nickname, password):
            return redirect('/login')
        else:
            return render_template('register.html', note='用户名已存在')
        # res = sql
    return render_template('register.html', note='欢迎注册')


@app.route('/user/<encrypted_code>/<user_id>')
def show_table(encrypted_code, user_id):
    """
    after sign in successfully, show the page for certain user by user_id
    :param encrypted_code: the encrypted_code is a str which can authenticate if this is a valid url.
    :param user_id: the id for the signed user
    :return: None
    """
    if not authentication(encrypted_code, user_id):
        return '无效路径，请注册登录'
    message_list = sql.message_search()
    message_list = [[i.nickname, i.content, i.time, i] for i in message_list]
    return render_template('table.html', message_list=message_list, cur_page=1, total_page=10, )


@app.route('/user/<encrypted_code>/<user_id>/profile')
def profile(encrypted_code, user_id):
    """
    get profile page of certain user
    """
    if not authentication(encrypted_code, user_id):
        return '无效路径，请注册登录'

    return render_template('profile.html')


@app.route('/user/<encrypted_code>/<user_id>/release')
def release(encrypted_code, user_id):
    """
    release a new message
    """
    if not authentication(encrypted_code, user_id):
        return '无效路径，请注册登录'

    return render_template('release.html')


@app.route('/user/<encrypted_code>/<user_id>/<message_id>')
def modify(encrypted_code, user_id, message_id):
    """
    modify a message
    """
    if not authentication(encrypted_code, user_id):
        return '无效路径，请注册登录'

    render_template('release.html')


def authentication(encrypted_code, user_id) -> bool:
    user = sql.user_search(user_id)
    if user is None or get_encrypted_code(user.password) != encrypted_code:
        return False
    return True


if __name__ == '__main__':
    app.run()
