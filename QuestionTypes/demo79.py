#判断‘https://blog.csdn.net’是否以‘http：//’或‘https：//’开头。若是，则返回‘http’或‘https’；否则，返回None
def get_url_start(url):
    # if url.startswith('http://') or url.startswith('https://'):
    if url.startswith(('http://','https://')):
        return url.split(':')[0]
    else:
        return None
url = 'https://blog.csdn.net'
print(get_url_start(url))
