#写一个函数，以0.1 秒的间隔不换行打印30 次由函数参数传入的字符，实现类似打字机的效果
import time

def slow_print(ch,n=30,delay=0.1):
    for i in range(n):
        print(ch,end='',flush=True)
        time.sleep(delay)
slow_print('*')