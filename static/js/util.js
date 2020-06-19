function jump2next(next) {
    var url = window.location.href;
    window.location.href = url.substring(0, url.lastIndexOf('/')) + '/' + next;
}
