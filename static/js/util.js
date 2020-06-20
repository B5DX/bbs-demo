function jump2next(next, if_new_window) {
    // 初期的页面跳转实现
    // 更好的方法是直接使用jinja调用url_for方法获取
    var url = window.location.href;
    var next_url = url.substring(0, url.lastIndexOf('/')) + '/' + next;
    if (if_new_window)
        window.open(next_url);
    else
        window.location.href = next_url;
}

function if_empty(value) {
    // 判断字符串value是否为空字符，空则返回true
    var re = /^\s*$/;
    var flag = re.test(value);
    return (value.length === 0 || flag);
}

function count_lines(s) {
    // 计算s中有几个'\n'，用于限制留言发布时过多行（要求小于等于3次换行）
    var cnt = 0;
    for (var i=0; i<s.length; i++) {
        if (s[i] === '\n') {
            cnt++;
        }
    }
    return cnt;
}