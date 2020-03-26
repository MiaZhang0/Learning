#数据的清洗,修改数据类型
import pandas as pd

path = r'E:\workspace\testdatas\sec_cars.csv'
data = pd.read_csv(path)
pd.set_option('display.max_rows',10) #设置最大显示行数
pd.set_option('display.max_columns',10) #设置最大显示列数
pd.set_option('display.width',500) #设置显示宽度
pd.set_option('display.max_colwidth',500) #设置打印宽度，有他没有···
pd.set_option('display.unicode.ambiguous_as_wide', True) #设置对齐
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('expand_frame_repr', False) #不换行
#查看前5行数据
print(data.head())
#查看各属性的数据类型
print(data.dtypes)
#改变Boarding_time的数据类型为datetime
data.Boarding_time = pd.to_datetime(data.Boarding_time,format = '%Y年%m月')
print(data.dtypes)
#将new_price转换为浮点型数据，需要将元素转换为字符型
data.New_price = data.New_price.str[:-1].astype(float)
print(data.dtypes)
