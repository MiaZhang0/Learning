# 进程间的通信
# 队列：先进先出
from multiprocessing import Queue
from multiprocessing import Process
import time


# q.put('') # 放元素
# q.get() # 取元素
# q.full() # 判断队列是否是满的
# q.empty() # 判断队列是否是空的
# q.qsize()  # 获取队列长度
def download(q):
    images = ['girl.jpg', 'boy.jpg', 'man.jpg']
    for image in images:
        print('正在下载：', image)
        time.sleep(0.5)
        q.put(image)


def getfile(q):
    while True:
        try:
            file = q.get(timeout=5)
            print('{}保存成功'.format(file))
        # 如果获取元素时超时5秒，那么说明元素取出完毕
        except:
            print('全部保存完毕！')
            break


if __name__ == '__main__':
    q = Queue(5)
    # 两个进程之间用的是同一个队列
    p1 = Process(target=download, args=(q,))
    p2 = Process(target=getfile, args=(q,))
    p1.start()
    p1.join()  # p1插队，现将p1执行完成再往下执行

    p2.start()
    p2.join()
