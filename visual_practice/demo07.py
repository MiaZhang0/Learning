#关系型数据的可视化，散点图的绘制
import pandas as pd
import matplotlib.pyplot as plt

path = r'E:\workspace\testdatas\iris.csv'
data = pd.read_csv(path)
#指定散点图的x轴数据，y轴数据，散点图中点的颜色
plt.scatter(x=data.Petal_Width,y=data.Petal_Length,color='steelblue')
#添加x轴和y轴标签
plt.xlabel('花瓣宽度')
plt.ylabel('花瓣长度')
#添加标题
plt.title('鸢尾花的花瓣宽度与长度关系')
#设置字体
plt.rcParams['font.sans-serif'] = ['SimHei']
#显示图形
plt.show()
#绘制气泡图
