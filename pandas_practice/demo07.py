#数据汇总
import pandas as pd
import numpy as np

path = r'E:\workspace\testdatas\diamonds.csv'
data = pd.read_csv(path)
# print(data)
#以颜色分类统计珠宝的平均价格
r1 = pd.pivot_table(data,index='color',values='price',aggfunc='mean')
#以颜色分类统计珠宝各清晰度的数量
r2 = pd.pivot_table(data,index='color',columns='clarity',aggfunc='size')
# print(r1)
# print(r2)
#通过groupby方法，指定分组变量
grouped = data.groupby(by=['color','cut'])
#对分组变量进行统计汇总
result = grouped.aggregate({'color': np.size,'carat': np.min, 'price': np.mean, 'table': np.max})
# print(result)
#调整变量名的顺序
result = pd.DataFrame(result,columns=['color','carat','price','table'])
#数据集重命名
result.rename(columns={'color': 'counts','carat': 'min_weight','price': 'avg_price','table': 'max_table'},inplace=True)
print(result)