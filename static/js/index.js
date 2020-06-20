// 用于index页面的js

function open_search_window() {
    // get base url
    var url = document.getElementById('search_form').action;
    // get ultimate url
    var keyword = document.forms['search_form']['keyword'].value
    var query = '?keyword=' + keyword;
    // empty input label
    document.forms['search_form']['keyword'].value = '';

    if (if_empty(keyword)) {
        alert('搜索框中内容为空');
        return false;
    }

    window.open(url+query);
    return false;
}

function page_jump() {
    // 输入页面点击跳转按钮时调用
    const next_page = document.forms['jump_form']['page'].value;
    const page_info = document.getElementById('page_info').innerHTML;
    const split_symbol_index = page_info.lastIndexOf('/')
    const max_page = page_info.substring(split_symbol_index+1, page_info.length);

    if (next_page <=0 || next_page > max_page) {
        document.forms['jump_form']['page'].value = '';
        alert('页面越界');
        return false;
    }
    return true;
}

function check_login_data() {
    // 检验登录数据的基本合法性
    const username = document.forms['login_form']['username'].value;
    const password = document.forms['login_form']['password'].value;

    const datas = [username, password];
    const result = datas.some(if_empty);

    if (result) {
        alert('用户名或密码不可为空');
        document.forms['login_form']['username'].value = '';
        document.forms['login_form']['password'].value = '';
        return false;
    }
    return true;
}