from flask import url_for, request, redirect, render_template, flash
from flask_login import current_user, login_user, logout_user
from module import sql, User, Message
from math import ceil
from app import app


@app.route('/')
def root():
    return redirect(url_for('index'))


@app.route('/index')
def index():
    """
    after sign in successfully, show the page for certain user by user_id
    :return: None
    """
    page = request.args.get('page', 1, type=int)
    message_length = sql.get_message_length()
    total_page = ceil(message_length / app.config['POSTS_PER_PAGE'])
    messages = Message.query.order_by(Message.time.desc()).paginate(
        page, app.config['POSTS_PER_PAGE'], False
    )
    next_url = url_for('index', page=messages.next_num) if messages.has_next else None
    pre_url = url_for('index', page=messages.prev_num) if messages.has_prev else None

    return render_template('index.html', message_list=messages.items, next_url=next_url,
                           pre_url=pre_url, cur_page=page.numerator, total_page=total_page)


@app.route('/login', methods=['POST'])
def login():
    """
    page for signing in.
    :return:
    if sign in successfully, redirect to a url for certain user
    else return templates 'sign.html'
    """
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    username = request.form['username']
    password = request.form['password']
    user = User.query.filter_by(username=username).first()

    if user is None or not user.check_password(password):
        flash('用户名或密码错误')
        return redirect(url_for('index'))

    login_user(user)
    return redirect(url_for('index'))


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
        username = request.form['username']
        password = request.form['password']
        repeat = request.form['repeat']
        # front side has checked the data, so the data here must be type valid.(maybe sql invalid, such as rename)
        if repeat != password:
            return render_template('register.html', note='两次输入的密码不同')
        elif sql.register(username, password):
            flash('注册成功')
            return redirect(url_for('index'))
        else:
            return render_template('register.html', note='用户名已存在')
        # res = sql
    return render_template('register.html', note='欢迎注册')


@app.route('/profile')
def profile():
    """
    get profile page of certain user
    """
    if not current_user.is_authenticated:
        return redirect(url_for('index'))
    messages = Message.query.filter_by(username=current_user.username).order_by(Message.time.desc()).all()
    return render_template('profile.html', username=current_user.username, my_messages=messages)


@app.route('/release', methods=['GET', 'POST'])
def release():
    """
    release a new message
    """
    if not current_user.is_authenticated:
        return redirect(url_for('index'))

    if request.method == 'POST':
        content = request.form['content']
        sql.insert_message(content, current_user.username)
        return redirect(url_for('index'))

    return render_template('release.html')


@app.route('/modify/<message_id>', methods=['GET', 'POST'])
def modify(message_id):
    """
    modify a message
    """
    if not current_user.is_authenticated:
        return redirect(url_for('index'))
    # 是否需要检测非法访问??

    if request.method == 'POST':
        sql.update(message_id, request.form['content'])
        return redirect(url_for('profile'))

    target_mes: Message = Message.query.filter_by(id=message_id).first()

    return render_template('release.html', message=target_mes)


@app.route('/search')
def search():
    keyword = request.args.get('keyword')
    result = sql.search_message(keyword)
    return render_template('search.html', message_list = result, keyword=keyword)


@app.route('/logout')
def logout():
    if not current_user.is_authenticated:
        return redirect(url_for('index'))

    logout_user()
    return redirect(url_for('index'))


@app.route('/delete/<message_id>')
def delete(message_id):
    sql.delete(message_id)
    # 未增加删除权限验证

    return redirect(url_for('profile'))


@app.route('/change_password', methods=['GET', 'POST'])
def change_password():
    if not current_user.is_authenticated:
        return redirect(url_for('index'))
    pass


if __name__ == '__main__':
    app.run()
