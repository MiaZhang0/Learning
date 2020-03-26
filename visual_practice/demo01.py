#绘制饼图
import matplotlib.pyplot as plt

#设置字体
plt.rcParams['font.sans-serif'] = ['SimHei']
edu = [0.2515,0.3724,0.3336,0.0368,0.0057]
labels = ['中专','大专','本科','硕士','其他']
#突出显示
explode = [0,0.1,0,0,0]
plt.pie(x=edu, labels=labels, explode=explode, autopct='%.1f%%')
plt.show()