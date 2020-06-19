from hashlib import md5

def check_str(target: str, s: str) -> bool:
    if len(s) > 20 or len(s) <= 0:
        return False
    if target == 'password':
        # only contain digit and alpha
        for i in s:
            if not (i.isalpha() or i.isdigit()):
                return False
    elif target == 'username':
        for i in s:
            if not (i.isalpha() or i.isdigit()) and not (u'\u4e00' <= i <= u'\u9fff'):
                return False
    return True


def encryption(password:str):
    secr = md5()
    secr.update(password.encode('utf-8'))
    return secr.hexdigest()


def get_encrypted_code(password) -> str:
    return str(password)[:10]


if __name__ == '__main__':
    test = '....'
    print(check_str(test, 'username'))