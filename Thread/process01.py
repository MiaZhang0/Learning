# 进程
'''
生活中的多任务场景：一边听歌，一边写作业；一边刷剧，一边吃饭···
电脑执行多任务：一边打开浏览器上网，一边听音乐，一边编代码

单核CPU实现多任务原理：操作系统轮流让各个任务交替执行，QQ执行2us，切换到微信，执行2us，再切换到其他程序···表面是每个任务反复执行，但CPU执行速度很快，给人同时进行的错觉
多核CPU实现多任务原理：执行多任务只能在多核CPU上实现，但由于任务数量远多于CPU的核心数量，所以，操作系统也会自动把很多任务轮流调度到每个核心上执行

并发：当有多个线程操作时，如果系统只有一个CPU，则它根本不及嗯呢该同时进行一个以上的线程，它只能把CPU运行时间划分成若干个时间段，
再将时间段分配给各个线程执行，在一个时间段的线程代码运行时，其他线程处于挂起状态。

并行：当系统有一个以上的CPU时，则线程的操作有可能非并发。当一个CPU执行一个线程时，另一个CPU可以执行另一个线程，两个线程互不抢占CPU资源，可以同时进行。

实现多任务的方式：（进程包含多个线程，线程包含多个协程）
1. 导包multiprocessing
2. p = Process(target=函数，name=进程的名字，args=(给函数传递的参数))
方法：
p.start()   启动进程并执行任务
p,run()     只是执行任务但没有启动进程
p.terminate()  终止

多进程对于全局变量访问，在每个全局变量里面都放一个m变量，保证每个进程访问变量互不干扰
'''
# 创建进程
from multiprocessing import Process
from time import sleep
import os

n = 0
list = []


def task1(s):
    global n
    while True:
        sleep(s)
        n += 1
        list.append(str(n) + 'task1')
        print('11111', os.getpid(), os.getppid(), n, list)


def task2(s):
    global n
    while True:
        sleep(s)
        n += 1
        list.append(str(n) + 'task2')
        print('22222', os.getpid(), os.getppid(), n, list)


# 主进程（主进程执行完之后会执行子进程）
if __name__ == '__main__':
    # 当前主进程
    print(os.getpid())
    # 子进程
    p1 = Process(target=task1, name='task1', args=(1,))
    # 启动进程任务1
    p1.start()
    p2 = Process(target=task2, name='task2', args=(2,))
    p2.start()
    while True:
        n += 1
        sleep(0.2)
        if n == 100:
            p1.terminate()
            p2.terminate()
            break
        else:
            print('-----number----', n)
    print('------------')


# 自定义进程
class MyProcess(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    # 重写run方法
    def run(self):
        m = 0
        while True:
            print('{}--进程名字:{}'.format(m, self.name))
            m += 1


if __name__ == '__main__':
    p3 = MyProcess('小明')
    p3.start()
    p4 = MyProcess('小红')
    p4.start()
