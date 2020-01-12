#分别根据每一行的首元素和尾元素大小对二维列表[[6,5],[3,7],[2,8]]排序
a = [[6,5],[3,7],[2,8]]
#根据每一行的首元素排序，默认reverse=Fasle，即排顺序
s = sorted(a,key=lambda x:x[0])
print(s)
#根据每一行的尾元素排序，设置reverse=True，即排倒序
d = sorted(s,key=lambda x:x[-1])
print(d)

