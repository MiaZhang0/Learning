# 异常：检查异常（IOException），由程序员处理，是人可以控制的；运行异常（RuntimeException），程序员无法处理的，只有等到异常出现后，再找到处理的办法。
# 异常处理
'''
try:
    可能出现异常的代码
except 异常类型（可能有多个）:
    如果有异常执行的代码
except Exception as err：
    print(err)  需要放最后，且err的内容就是错误原因
finally:
    无论是否存在异常都会被执行的代码
    （应用场景：文件读写操作，无论是否存在异常，文件最后都会被关闭；数据库操作，无论是否存在异常，数据库都会被关闭，释放内存）
else：
    如果try中没有发生异常则执行的代码
注意：1.如果使用else则在try代码中不能出现return；2.try，finally中有return时，会执行完finally中的return
'''


# 抛出异常：自定义异常raise；系统异常ValueError,·····
# 注册 用户名必须6位
def register():
    username = input('输入用户名：')
    if len(username) < 6:
        raise Exception('用户长度必须6位以上')
    else:
        print('输入的用户名是：', username)


try:
    register()
except Exception as err:
    print(err)
    print('注册失败')
else:
    print('注册成功')
