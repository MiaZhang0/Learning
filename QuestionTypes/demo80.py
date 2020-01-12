#判断‘https://blog.csdn.net’是否以‘.com’或‘.net’结束。若是，则返回‘com’或‘net’；否则，返回None
def get_url_end(url):
    if url.endswith(('.com','.net')):
        return url.split('.')[-1]
    else:
        return None
url = 'https://blog.csdn.net'
print(get_url_end(url))