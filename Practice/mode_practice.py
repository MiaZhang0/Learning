# 开发模式：单例模式，优化内存地址，节省内存。对于一个类，保证开发者在使用时使用的是一个地址，但并不是说有的类都适合单例模式
class Singleton:
    # 私有化 单例的地址存在__instance__
    __instance = None

    # 重写__new__
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            # new函数创建一个地址并赋值给instance
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance

    # return执行完毕后会先执行__init__，再出类
    def show(self):
        print('--------')


# s = Singleton()
# print(dir(s))
# print(dir(Singleton))
'''
在python中，模块是代码组织的一种方式，把功能相近的函数放到一个文件中，一个文件（.py）就是一个模块（module），模块名就是文件名。
--提高代码的可复用、可维护性。一个模块编写完毕后，可以很方便的在其他项目中导入
--解决了命名冲突，不同模块中相同的命名不会冲突
'''
# from 模块名 import *  引用模块中所有的类，方法，变量 ，限制获取的内容，在模块中使用__all__ = [想要引用的内容]
# 无论是import还是from形式，都会将模块内容进行加载，如果不希望其进行调用，就会用到__name__
# 在源模块中__name__ == __main__，但如果在其他模块中用from导入模块时，__name__等于导入的模块名
'''
文件夹与包的区别：文件夹中存放非py文件，而包中仅存放py文件；如果将__init__.py存放到文件夹中，该文件夹就会变成包
'''

# 导包时，会默认执行__init__.py
'''
__init__.py的作用：
1. 导包时，把一些初始化的函数，变量，类定义在__init__.py文件中
2. 访问方式：包名.函数（变量，类）
3. 在__init__.py中加入__all__ = [模块名1，模块名2，···]，可以使用from 包名 import * 来调用包中的模块
'''
# 模块的循环导入(大型项目中存在许多py文件，架构不清晰就容易导致循环导入)
'''
# 避免循环导入的方法：
1. 重新架构；
2.将导入的语句放到函数里面；
3.将导入的语句放到模块的最后
'''
# 当你导入一个模块，python解析器对模块位置的搜索顺序是：
'''
1. 当前目录
2. 如果不在当前目录，python则搜索在shell  变量  python path 下的每个目录
3. 如果都找不到，python会查看默认路径。Unix环境默认路径是/usr/local/lib/python
模块搜索路径存储在system 模块的 sys.path 变量中。变量里包含当前，目录，PYTHON PATH和安装过程决定的默认目录。
'''
import sys

print(sys.path)
print(sys.version)
print(sys.argv)  # 运行程序时的参数，argv是一个列表
import time

# 1. 时间戳
t = time.time()
# 2. 将时间戳转成字符串
time.ctime(t)
# 将时间戳转成元组，可以获取年月日时分秒
t1 = time.localtime(t)
# 将元组转成时间戳
time.mktime(t1)
# 将元组的时间转成字符串，即格式化时间
t2 = time.strftime('%Y-%m-%d %H:%M:%S')
print(t2)
# 将字符串转成元组时间
t3 = time.strptime('2020.12.12', '%Y.%m.%d')
print(t3)
import datetime

print(datetime.time.hour)  # 返回的是时间对象
# date是一个类
d = datetime.date(2020, 12, 12)
print(datetime.date.day)
print(datetime.date.ctime(d))
# 获取今日日期
print(datetime.date.today())
# timedelta是一个时间差与now()结合使用
h1 = datetime.timedelta(hours=2)  # 支持天，周，小时···
now = datetime.datetime.now()
print(now)
result = now + h1
print(result)
# 时间差的应用场景
# 缓存：数据redis，让数据保存相应的时间，作为缓存，Redis.set(key,value,时间差)，会话：session
import random

r1 = random.randrange(1, 20, 2)  # randrange(start,stop,step),默认step=1
r2 = random.randint(1, 10)
list = ['zxm', 'haha', 'klkl']
# 随机选择列表中的内容
r3 = random.choice(list)
# 打乱顺序
list1 = ['if', 'else', 'qwe', 'local']
r4 = random.shuffle(list1)


# 获取验证码
def getcode():
    code = ''
    for i in range(4):
        r1 = str(random.randint(0, 9))
        # 将数字转换成字母
        r2 = chr(random.randint(65, 90))
        r3 = chr(random.randint(97, 122))
        r = random.choice([r1, r2, r3])
        code += r
    return code


print(getcode())
# 将字母转换成Unicode码
ord('A')
ord('上')
# 标准库
# print() input() list() str() dict() tuple() int() chr() ord() bin() hex() oct() isinstance()
# 加密算法 （只有知道算法底层才能解密的算法md5,sha1 sha256），BASE64可逆
import hashlib
msg = '中午一起吃饭'
# 不能直接传中文字符，必须编码
md5_msg = hashlib.md5(msg.encode('utf-8'))
# 转成16进制
print(md5_msg.hexdigest())

sha1_msg = hashlib.sha1(msg.encode('utf-8'))
print(sha1_msg.hexdigest())

sha256_msg = hashlib.sha256(msg.encode('utf-8'))
print(sha256_msg.hexdigest())

# 判断用户的密码是否正确，需要将输入密码加密后与数据库中的加密值对比是否一致
# 第三方应用模块，图片处理模块pillow
import Pillow