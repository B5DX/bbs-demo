function jump(url) {
    window.location.href = url;
}

function if_empty(value) {
    // return true if parameter 'value' is empty string
    // else return false
    const re = /^\s*$/;
    const flag = re.test(value);
    return (value.length === 0 || flag);
}

function count_lines(s) {
    // count the '\n' in string s
    // used to limit too many lines when a message is posted
    // it is required to wrap lines less than or equal to 3 times
    let cnt = 0;
    for (let i=0; i<s.length; i++) {
        if (s[i] === '\n') {
            cnt++;
        }
    }
    return cnt;
}