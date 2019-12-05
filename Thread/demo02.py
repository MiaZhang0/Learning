'''
线程锁Lock（互斥锁）：避免资源竞争冲突（当有很多子线程时，刚开始可能还是顺序执行，但到后来多个子线程同时执行造成冲突）。
Lock只能有一个线程获取，获取该锁的线程才能执行，否则阻塞；执行完任务后，必须释放锁。
演示代码如下：
'''

# -*- encoding: utf8 -*-

import time
import threading

lock = threading.Lock()  # 创建互斥锁
counter = 0  # 计数器

def hello():
    """线程函数"""

    global counter

    if lock.acquire():  # 请求互斥锁，如果被占用，则阻塞，直至获取到锁
        time.sleep(0.2)  # 假装思考、敲键盘需要0.2秒钟
        counter += 1
        print('我是第%d个' % counter)

    lock.release()  # 千万不要忘记释放互斥锁，否则后果很严重

def demo():
    threads = list()
    for i in range(30):  # 假设群里有30人，都喜欢吃苹果
        threads.append(threading.Thread(target=hello))
        threads[-1].start()

    for t in threads:
        t.join()

    print('统计完毕，共有%d人' % counter)

if __name__ == '__main__':
    demo()