from hashlib import md5


def encryption(password: str):
    """
    Encrypt the raw password using md5.
    :param password: raw password
    :return: An encrypted password.
    """
    secr = md5()
    secr.update(password.encode('utf-8'))
    return secr.hexdigest()
