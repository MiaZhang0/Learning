# 协程：微线程,应用场景：耗时操作（网络请求、网络下载如爬虫、网络上传或其他IO操作如文件的读写、阻塞）
# 协程由生成器完成
import time
from greenlet import greenlet
import gevent
from gevent import monkey

# 添加monkey补丁，将sleep方法已经换成monkey里面的sleep
monkey.patch_all()


def a():
    for i in range(5):
        print('A' + str(i))
        # gb.switch()
        time.sleep(0.1)


def b():
    for i in range(5):
        print('B' + str(i))
        # gc.switch()
        time.sleep(0.1)


def c():
    for i in range(5):
        print('C' + str(i))
        # ga.switch()
        time.sleep(0.1)


if __name__ == '__main__':
    # ga = greenlet(a)
    # gb = greenlet(b)
    # gc = greenlet(c)
    # ga.switch()

    g1 = gevent.spawn(a)
    g2 = gevent.spawn(b)
    g3 = gevent.spawn(c)
    g1.join()
    g2.join()
    g3.join()
    print('END')
