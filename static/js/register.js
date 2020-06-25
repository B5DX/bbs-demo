function check_register_data() {
    // check data on register page
    let username = document.forms['reg_form']['username'].value;
    let password = document.forms['reg_form']['password'].value;
    let repeat_password = document.forms['reg_form']['repeat'].value;

    if ( repeat_password !== password ) {
        alert('两次输入的密码不相同');
        document.getElementById('username').value = '';
        document.getElementById('password').value = '';
        document.getElementById('repeat').value = '';
        return false;
    }

    let flag = check_length(username, 'username') && check_length(password, 'password');
    if (!flag) {
        alert('用户名或密码长度不符合要求');
        document.getElementById('username').value = '';
        document.getElementById('password').value = '';
        document.getElementById('repeat').value = '';
        return false;
    }
    // username: digits or A-z or Chinese
    flag = check_type(username, 'username') && check_type(password, 'password');
    if (!flag) {
        alert('用户名或密码输入类型不符合要求');
        document.getElementById('username').value = '';
        document.getElementById('password').value = '';
        document.getElementById('repeat').value = '';
        return false;
    }

    return true;
}

function check_length(s, data_type) {
    // check data length
    // data_type can be 'password' or 'username'
    // return true length is valid
    if (data_type === 'password')
        return (s.length >= 5 && s.length <= 20);
    else
        return (s.length >= 1 && s.length <= 15);
}

function check_type(s, data_type) {
    // check data type
    // data_type can be 'password' or 'username'
    // return true if data is valid
    if (data_type === 'password') {
        let re = /[^A-z0-9]/;
        return  !re.test(s);
    } else {
        let re = /[^\u4e00-\u9fa5A-z0-9]/;
        return !re.test(s);
    }
}