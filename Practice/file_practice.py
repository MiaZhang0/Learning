# 文件操作
'''
文件上传、下载、复制
'''
# read()      读取文件
# readable()  判断文件是否可读
# readline()  读取一行
# readlines() 读取文件，返回值是一个列表
# writable() 判断文件是否可写
# write()     写文件
# writelines(iterable)  可将列表中的信息写入文件
# close()     关闭文件

import os

'''
python模块：XXX.py
'''
# os.path.dirname(__file__) # 获取当前文件所在的文件目录（绝对路径）
# os.path.join(path,文件名)  # 返回的是拼接后的新路径
# rfind('\\')  截取文件名
r = os.path.isabs('..\python100\day01\demo01.py')  # 判断是否是相对路径，其中..\表示返回上一级
print(r)
path = os.path.abspath('文件名')  # 通过相对路径得到绝对路径
print(path)
path1 = os.getcwd()  # 获取当前的工作目录

r1 = os.path.split(path)  # 获取路径下的文件名
print(r1[1])

r2 = os.path.splitext(path)  # 获取路径下的文件名的后缀，用于判断文件类型
print(r2[1])

r3 = os.path.getsize(path)  # 获取文件的大小，单位是字节
print(r3)

all = os.listdir(path)  # 返回指定目录下的所有文件和文件夹，保存到列表中

os.path.exists(path)  # 判断路径是否存在
os.mkdir(path)  # 创建文件夹
os.rmdir(path)  # 只能删除空的文件夹
os.removedirs(path)
os.remove(path)  # 删除文件
# 删除非空文件夹
filelist = os.listdir(path)
for file in filelist:
    path1 = os.path.join(path, file)
    os.remove(path1)
else:
    os.rmdir(path)
# 切换目录
os.chdir(path)

# 复制文件（包含多层文件夹）
src_path = ''
target_path = ''


def copy(src, target):
    # 获取文件夹里面的内容
    filelist = os.listdir(src)
    # 遍历文件列表
    for file in filelist:
        # 拼接路径
        path = os.path.join(src, file)
        # 判断是文件夹还是文件
        if os.path.isdir(path):
            # 递归调用copy
            copy(path, target)
        else:
            # 不是文件夹则直接进行复制
            with open(path, 'rb') as rstream:
                container = rstream.read()

                path2 = os.path.join(target, file)
                with open(path2, 'wb') as wstream:
                    wstream.write(container)
    else:
        print('复制完毕')


copy(src_path, target_path)
