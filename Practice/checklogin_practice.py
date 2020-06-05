# 登录验证
import time


# 定义一个登录函数
def login():
    user = input('请输入用户名：')
    pwd = input('请输入密码：')
    if user == 'zxm' and pwd == '123':
        return True
    else:
        print('用户名或密码错误')
        return False


islogin = False  # 默认没有登录


# 定义一个装饰器，进行付款验证
def login_required(f):
    def wrapper(*args, **kwargs):
        global islogin
        print('--------付款----------')
        # 验证用户是否登录
        if islogin:
            f(*args, **kwargs)
        else:
            print('登录后才能付款')
            # 跳转登录页面
            islogin = login()
            print('result:', islogin)

    return wrapper


@login_required
def pay(money):
    print('正在付款，付款金额是：{}元'.format(money))
    print('正在付款中····')
    time.sleep(3)
    print('付款完成')


pay(100)
pay(89)
