#外部数据的读取，文本数据
#engine='python'没有他会有警告，
import pandas as pd

path = r'E:\workspace\testdatas\data_test01.txt'
data = pd.read_csv(path,skiprows=2,sep=',',skipfooter=3,converters={'id':str},encoding='utf-8',thousands='&',
                     header=None,names=['id','year','month','day','gender','occupation','income'],usecols=['id','occupation','income'],engine='python')
print(data)

