#数据的清洗，缺失值的识别与处理
import pandas as pd

path = r'E:\workspace\testdatas\data_test05.xlsx'
data = pd.read_excel(path)
# print(data)
# print(data.isnull())
print(data.isnull().any(axis=0))
#计算缺失值,每行的总和除以列数
result = data.isnull().sum(axis=0)/data.shape[0]
print(result)
#删除缺失行
print(data.dropna())
#填充法,性别的众数，年龄的平均数，收入的中位数
data.fillna(value={'gender':data.gender.mode()[0],'age':data.age.mean(),'income':data.income.median()},inplace=True)
print(data)