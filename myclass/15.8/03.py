import re


def check_phone(strphone):
    regex_phone = re.compile(r'^(\(\d{3}\)|\d{3}-)?\d{8}$')
    result = True if regex_phone.match(strphone) else False
    return result


def check_ZIP(strZIP):
    regex_ZIP = re.compile(r'^\d{6}$')
    result = True if regex_ZIP.match(strZIP) else False
    return result


def check_URL(strURL):
    regex_URL = re.compile(r'^https?://\w+(?:\.[^\.]+)+(?:/.+)*$')
    result = True if regex_URL.match(strURL) else False
    return result


print(check_phone("18622412361"))
print(check_URL("https://www.baidu.com"))
