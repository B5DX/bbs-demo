function validate_data() {
    // 检验注册页面上传的数据是否合法
    username = document.forms['reg_form']['username'].value;
    password = document.forms['reg_form']['password'].value;
    repeat_password = document.forms['reg_form']['repeat'].value;

    if ( repeat_password !== password ) {
        alert('两次输入的密码不相同');
        document.getElementById('username').value = '';
        document.getElementById('password').value = '';
        document.getElementById('repeat').value = '';
        return false;
    }

    var flag = false;
    if ( username.length <= 0 || username.length >= 20 ) {
        flag = true;
    }
    if ( password.length <= 0 || password.length >= 20 ) {
        flag = true
    }
    if (flag) {
        alert('昵称或密码长度不符合要求');
        document.getElementById('username').value = '';
        document.getElementById('password').value = '';
        document.getElementById('repeat').value = '';
        return false;
    }
    // username: digits or A-z or Chinese
    var re = /[^\u4e00-\u9fa5A-z0-9]/;
    flag = re.test(username);
    // password: digits or A-z
    re = /[^A-z0-9]/;
    flag = flag || re.test(password);
    if (flag) {
        alert('昵称或密码输入类型不符合要求');
        document.getElementById('username').value = '';
        document.getElementById('password').value = '';
        document.getElementById('repeat').value = '';
        return false;
    }

    return true;
}