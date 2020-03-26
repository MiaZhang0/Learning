#外部数据的读取，Excel数据
import pandas as pd

path = r'E:\workspace\testdatas\data_test02.xlsx'
data = pd.read_excel(path,header=None,names=['ID','Product','Color','Size'],converters={'ID':str})
print(data)
