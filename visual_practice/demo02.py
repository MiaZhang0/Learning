#绘制条形图
import pandas as pd
import matplotlib.pyplot as plt

path = r'E:\workspace\testdatas\Province GDP 2017.xlsx'
GDP = pd.read_excel(path)

#纵向条形图
#设置绘图风格
plt.style.use('ggplot')
#对读入数据做升序排序
GDP.sort_values(by='GDP',inplace=True)
#指定条形图x轴的刻度值（shape返回行数），y轴的数值，x轴的刻度标签，填充色
plt.bar(x=range(GDP.shape[0]),height=GDP.GDP,tick_label=GDP.Province,color='steelblue')
#添加y轴的标签
plt.ylabel('GDP(万亿)')
#添加条形图的标题
plt.title('2017年度6个省份GDP分布')
#为每个条形图添加数值标签
for x,y in enumerate(GDP.GDP):
    plt.text(x,y+0.1,'%s'%round(y,1),ha='center')
#设置字体
plt.rcParams['font.sans-serif'] = ['SimHei']
#显示图形
plt.show()
print('*********************************************')
#横向条形图
plt.style.use('ggplot')
GDP.sort_values(by='GDP',inplace=True)
plt.barh(y=range(GDP.shape[0]),width=GDP.GDP,tick_label=GDP.Province,color='steelblue')
plt.xlabel('GDP(万亿)')
plt.title('2017年度6个省份GDP分布')
for y,x in enumerate(GDP.GDP):
    plt.text(x+0.1,y,'%s'%round(x,1),ha='center')
plt.show()