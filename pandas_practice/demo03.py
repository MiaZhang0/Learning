#外部数据的读取，数据库
import pandas as pd
import pymysql

bridge = pymysql.connect(host='localhost',user='root',password='Kk12345',database='test')
data = pd.read_sql('select * from members',con=bridge)
#避免占用内存资源
bridge.close()
print(data)

#返回表的行数与列数
print(data.shape)
#返回表的列名称
print(data.columns)
#返回数据类型
print(data.dtypes)
# describe默认对数值型数据进行统计，count为统计是否有缺省，非数值变量的统计描述用describe（include=‘object’）
print(data.describe(include='object'))
#筛选姓名列
print(data.name)#或者print(data["name"])
#行筛选
print((data.loc[data['id'] == 5,:]))
#行列的筛选
result = data.loc[(data['occupation'] == 'R&D Engineer') & (data['income'] > 15000),['id','name']]
print(result)