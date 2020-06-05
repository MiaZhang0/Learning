'''
进程池：需要创建的子进程数量不多时，可以直接利用multiprocessing中的Process动态生成多个进程。
如果需要更多的目标（百个以上），手动创建进程的工作量很大，因此需要用到multiprocessing模块中的Pool方法。
初始化Pool时，指定一个最大进程数，当有新的请求提交到Pool时，如果池还没有满，那么会创建一个新的进程用来执行该请求；
如果达到最大值，该请求会等待，知道池中有进程结束，才会创建新的进程来执行。

非阻塞式：一次性将任务全部添加到队列中，进程池中执行完任务后（各自进行互不干扰），回调函数才调用
阻塞式：添加一个任务，执行一个任务，第一个任务结束后，第二个任务才能添加。类似于循环，不是队列，没有使用进程的优势。
'''

import os
from multiprocessing import Pool
import time
from random import random

container = []


def task(task_name):
    print('----start------', task_name)
    start = time.time()
    time.sleep(random() * 2)
    end = time.time()
    # print('{}完成，用时：{}，进程id：{}'.format(task_name,(end - start),os.getpid()))
    return '{}完成，用时：{}，进程id：{}'.format(task_name, (end - start), os.getpid())


# 回调函数
def callback_func(n):
    container.append(n)

# 非阻塞式
if __name__ == '__main__':
    # 创建进程池对象
    pool = Pool(5)
    tasks = ['踢球', '做作业', '练瑜伽', '练钢琴', '画画', '练舞', '练字']
    for task1 in tasks:
        # 非阻塞的
        pool.apply_async(task, args=(task1,), callback=callback_func)
    # 停止添加进程
    pool.close()
    # 让主进程让步（插队）
    pool.join()
    for i in container:
        print(i)
    print('over·····')

# 阻塞式
if __name__ == '__main__':
    pool = Pool(5)
    tasks = ['踢球', '做作业', '练瑜伽', '练钢琴', '画画', '练舞', '练字']
    for task1 in tasks:
        # 阻塞的
        pool.apply(task,args=(task1,))
    pool.close()
    pool.join()
    print('over·····')