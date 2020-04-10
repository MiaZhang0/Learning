#利用numpy模块将列表转化为数组，并对数组进行运算
import numpy as np

list = [[1,2,3],[4,5,6],[7,8,9]]
#将二维列表转换成二维数组
array = np.array(list)
print(array)
#计算每一行的和，结果是3行1列的矩阵，瘦axis=1
sum = []
for row in range(3):
    sum.append(np.sum(array[row,:]))
print(sum)

sum1 = array.sum(axis=1)
print(sum1)
sum2 = np.sum(array,axis=1)
print(sum2)

#计算每一列的平均值,结果是1行3列的矩阵，胖axis=0
avg = []
for col in range(3):
    avg.append(np.mean(array[:,col]))
print(avg)
#avg是一个列表
print(type(avg))
#avg1是一个数组
avg1 = array.mean(axis=0)
print(avg1)
print(type(avg1))
avg2 = np.mean(array,axis=0)
print(avg2)