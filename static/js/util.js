function jump(url) {
    // 页面跳转
    window.location.href = url;
}

function if_empty(value) {
    // 判断字符串value是否为空字符，空则返回true
    const re = /^\s*$/;
    const flag = re.test(value);
    return (value.length === 0 || flag);
}

function count_lines(s) {
    // 计算s中有几个'\n'，用于限制留言发布时过多行（要求小于等于3次换行）
    let cnt = 0;
    for (let i=0; i<s.length; i++) {
        if (s[i] === '\n') {
            cnt++;
        }
    }
    return cnt;
}