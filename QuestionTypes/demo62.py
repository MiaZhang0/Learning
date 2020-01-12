#从键盘输入手机号码，输出形如‘Mobile: 186 6677 7788’的字符串
def print_mobile():
    num = input('请输入手机号码：')
    print('Mobile: %s %s %s'%(num[:3],num[3:7],num[7:]))
print_mobile()