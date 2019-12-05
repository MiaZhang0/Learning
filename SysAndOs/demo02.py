'''
应用例子：设计一个多项求和的脚本，从命令行读取参数参与求和的各个数字。
'''
# -*- coding:utf-8 -*-

import sys

def multi_sum(args):
    return sum(args)

if __name__ == '__main__':
    print(sys.argv)
    args = sys.argv[1:]
    result = multi_sum([float(item) for item in args])
    print('输入了%d个参数'%len(args))
    print('累计和为%f'%result)
