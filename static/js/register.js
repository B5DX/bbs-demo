function validate_data() {
    nickname = document.forms['reg_form']['nickname'].value;
    password = document.forms['reg_form']['password'].value;
    var flag = false;
    if ( nickname.length <= 0 || nickname.length >= 20) {
        flag = true;
    }
    if ( password.length <= 0 || password.length >= 20) {
        flag = true
    }
    if (flag) {
        alert('昵称或密码长度不符合要求');
        document.getElementById('nickname').value = '';
        document.getElementById('password').value = '';
        return false;
    }
    // nickname: digits or A-z or Chinese
    var re = /[^\u4e00-\u9fa5A-z0-9]/;
    flag = re.test(nickname);
    // password: digits or A-z
    re = /[^A-z0-9]/;
    flag = flag || re.test(password);
    if (flag) {
        alert('昵称或密码输入类型不符合要求');
        document.getElementById('nickname').value = '';
        document.getElementById('password').value = '';
        return false;
    }
    return true;
}