#从键盘输入年月日时分秒，输出形如‘2019-05-01 12:00:00’的字符串
def print_datetime():
    dt = input('请输入年月日时分秒，中间以空格分隔：')
    Y,M,D,h,m,s = dt.split()
    Y,M,D,h,m,s = int(Y),int(M),int(D),int(h),int(m),int(s)
    print('%04d-%02d-%02d %02d:%02d:%02d'%(Y,M,D,h,m,s))
print_datetime()