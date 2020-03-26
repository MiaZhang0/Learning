#绘制折线图

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

path = r'E:\workspace\testdatas\wechat.xlsx'
data = pd.read_excel(path)
#设置x轴数据,y轴数据，折线类型，折线宽度，折线颜色，折线图中添加圆点，点的大小，点的边框色，点的填充色
# 折线类型'-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'
plt.plot(data.Date,data.Counts,linestyle='-',linewidth=2,color='steelblue',marker=0,markersize=2,markeredgecolor='black',markerfacecolor='red')
#添加y标签
plt.ylabel('人数')
#添加图形标题
plt.title('每天微信文章阅读人数趋势')
#设置字体
plt.rcParams['font.sans-serif'] = ['SimHei']
#获取图的坐标信息
ax = plt.gca()
#设置日期的显示格式
date_format = mdates.DateFormatter('%m/%d')
ax.xaxis.set_major_formatter(date_format)
#设置x每个刻度的间隔天数
xlocator = mdates.ticker.MultipleLocator(7)
ax.xaxis.set_major_locator(xlocator)
#显示图形
plt.show()