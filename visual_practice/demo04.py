#绘制直方图
import pandas as pd
import matplotlib.pyplot as plt

path = r'E:\workspace\testdatas\titanic_train.csv'
Titanic = pd.read_csv(path)

#检查年龄是否有缺失（如果数据中存在缺失值，将无法绘制直方图）
any(Titanic.Age.isnull())
#不妨删除含有缺失年龄的观察
Titanic.dropna(subset=['Age'],inplace=True)
#绘制直方图
plt.hist(x=Titanic.Age,bins=20,color='steelblue',edgecolor='black')
#添加x轴和y轴标签
plt.xlabel('年龄')
plt.ylabel('频数')
#添加标题
plt.title('乘客年龄分布')
#设置字体
plt.rcParams['font.sans-serif'] = ['SimHei']
#显示图形
plt.show()