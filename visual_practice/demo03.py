#绘制双条形图，水平交错条形图
import pandas as pd
import matplotlib.pyplot as plt

path = r'E:\workspace\testdatas\HuRun.xlsx'
HuRun = pd.read_excel(path)
#制作透视表
HuRun_reshape = HuRun.pivot_table(index='City', columns='Year', values='Counts').reset_index()
#对数据集降序排序
HuRun_reshape.sort_values(by=2016,ascending=False,inplace=True)
HuRun_reshape.plot(x='City',y=[2016,2017],kind='bar',color=['steelblue','indianred'],rot=0,width=0.8,title='近两年5个城市亿万资产家庭数比较')
#添加y轴标签
plt.ylabel('亿万资产家庭数')
plt.xlabel('')
#设置字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.show()

