#数据的清洗,冗余数据的识别与处理
import pandas as pd

path = r'E:\workspace\testdatas\data_test04.xlsx'
data = pd.read_excel(path)
print(data)
#查看数据是否有冗余（是否有完全相同的行,或者关系中某一个属性是否重复）
result = data.duplicated(subset='appname')
print(result)
#删除冗余数据,inplace默认为False，即如果直接使用drop_duplicates()不会直接删除关系中的冗余数据
data.drop_duplicates(inplace=True)
print(data)