// js for index.html

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
    // the pagination 'jump' button on index.html will call this function
    // check if the input page is valid
    const next_page = Number(document.forms['jump_form']['page'].value);
    const page_info = document.getElementById('page_info').innerHTML;
    const split_symbol_index = page_info.lastIndexOf('/')
    const max_page = Number(page_info.substring(split_symbol_index+1, page_info.length));

    if (next_page <=0 || next_page > max_page) {
        document.forms['jump_form']['page'].value = '';
        alert('页面不合法');
        return false;
    }
    return true;
}

function check_login_data() {
    // validation login data
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