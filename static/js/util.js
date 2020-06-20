function jump2next(next, if_new_window) {
    var url = window.location.href;
    var next_url = url.substring(0, url.lastIndexOf('/')) + '/' + next;
    if (if_new_window)
        window.open(next_url);
    else
        window.location.href = next_url;
}

function if_empty(value) {
    var re = /[^\S*&]/;
    var flag = re.test(value);
    return (value.length === 0 || flag);
}