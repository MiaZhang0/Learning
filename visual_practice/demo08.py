#绘制热力图seaborn
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

path = r'E:\workspace\testdatas\Sales.xlsx'
data = pd.read_excel(path)
#根据交易日期，衍生出年份和月份字段
data['year'] = data.Date.dt.year
data['month'] = data.Date.dt.month
#统计每年各月份的销售总额（绘制热力图之前，必须将数据转换为交叉表形式即透视表）
summary = data.pivot_table(index='month',columns='year',values=data,aggfunc=np.sum)
print(summary)
#绘制热力图，指定绘图数据，指定填充色，设置每个单元格边框的宽度，显示数值，以科学计算法显示数据
sns.heatmap(data=summary,cmap='PuBuGn',linewidths=0.1,annot=True,fmt='.1e')
#添加标题
plt.title('每年各月份销售总额热力图')
plt.xlabel(xlabel='year')
#设置字体
plt.rcParams['font.sans-serif'] = ['SimHei']
#显示图形
plt.show()