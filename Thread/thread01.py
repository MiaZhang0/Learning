# 线程（最小单元）属于进程，依赖于进程。一个进程中有多个线程，多个线程共用进程资源
# 线程状态： 新建 --start-- 就绪 --run-- 结束
#                          阻塞
# 共享数据
# python支持小中型的项目，大型项目还是需要java
'''
如果多个线程共同对某个数据修改，则可能出现不可预料的结果，为了保证数据的正确性，需要对多个线程进行同步
'''
# 同步：一个一个的完成，一个做完另一个才能进来。影响：速度慢，效率低。
'''使用Tread对象的Lock和RLock可以实现简单的线程同步，这两个对象都有acquire方法和release方法，
对于那些需要每次只允许一个线程操作的数据，可以将其操作到acquire和release方法之间。
多线程的优势在于可以同时运行多个任务。但是当线程需要共享数据时，可能存在数据不同步的问题，因此便引入了锁的概念。

一般来说，在共享数据时（计算量小时），用线程会造成数据不安全，但是python不会，它底层会自动加锁，只有当计算量大到一定程度，这个锁才会释放
因此，python的线程，又叫“伪线程”。
线程是可以共享全局变量的
GIL(Global Interpreter Lock) 全局解释器锁：python底层只要用线程默认加锁，形成线程同步，虽然数据安全但会造成速度慢，不是纯线程。
GIL会释放的条件：计算量大
GIL并不是Python的特性，Python完全可以不依赖于GIL.它是在实现Python解析器(CPython)时所引入的一个概念,JPython就没有GIL

线程使用场景： 耗时操作，爬虫、IO
进程使用场景：计算密集型，为了数据安全需要手动加锁，解锁
'''

import threading
import time


def download():
    images = ['girl.jpg', 'boy.jpg', 'man.jpg']

    for image in images:
        print('正在下载：', image)
        time.sleep(0.5)  # 阻塞状态，不占用进程资源，进程的资源就会给到别的线程
        print('下载{}成功'.format(image))


def listenmusic():
    musics = ['123', '456', '789']
    for music in musics:
        time.sleep(0.5)  # 阻塞状态，不占用进程资源，进程的资源就会给到别的线程
        print('真在听{}歌'.format(music))


# 创建线程对象
# t1 = threading.Thread(target=download, name='aa')
# t1.start()
#
# t2 = threading.Thread(target=listenmusic, name='bb')
# t2.start()

# 创建锁对象
lock = threading.Lock()
list1 = [0] * 10


def task1():
    # 获取线程锁，如果已经上锁，则等待锁的释放，只要不释放，其他线程就无法进行运行状态
    lock.acquire()  # 阻塞
    for i in range(len(list1)):
        list1[i] = 1
        time.sleep(0.5)
    lock.release()  # 释放锁


def task2():
    lock.acquire()
    for i in range(len(list1)):
        print(list1[i])
        time.sleep(0.5)
    lock.release()


# if __name__ == '__main__':
#     t1 = threading.Thread(target=task1)
#     t2 = threading.Thread(target=task2)
#
#     t1.start()
#     t2.start()
# 死锁的概念
'''
开发过程中使用线程，在线程间共享多个资源的时候，如果两个线程分别占有一部分资源并且同时等待对方的资源，就会造成死锁。
尽管死锁很少发生，但一旦发生就会造成应用的停止响应，程序不会做任何事情

避免死锁：1.重构代码 2.在acquire中加入参数timeout
'''
from threading import Thread, Lock

lockA = Lock()
lockB = Lock()


class MyThread(Thread):
    def run(self):
        # 如果可以获取到锁则返回True
        if lockA.acquire():
            print(self.name + 'A锁')  # self.name在没有init方法的情况下，系统会默认取名
            time.sleep(0.1)
            if lockB.acquire(timeout=5):
                print(self.name + 'B锁 + A锁')
                lockB.release()
            lockA.release()


class MyThread1(Thread):
    def run(self):
        # 如果可以获取到锁则返回True
        if lockB.acquire():
            print(self.name + 'B锁')  # self.name在没有init方法的情况下，系统会默认取名
            time.sleep(0.1)
            if lockA.acquire(timeout=5):
                print(self.name + 'A锁 + B锁')
                lockA.release()
            lockB.release()


if __name__ == '__main__':
    t1 = MyThread()
    t2 = MyThread1()

    t1.start()
    t2.start()
