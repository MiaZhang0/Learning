# 绘制y = x的平方曲线
import numpy as np
import matplotlib.pyplot as plt

# 数据准备
x = np.arange(-10, 11, 1)  # 或者np.linspace(-5,6,100)
y = x ** 2  # y=pow(x,2)

# 图纸绘制部分
fig = plt.figure()
ax = fig.add_subplot()
plt.plot(x, y)

# 图像保存显示
plt.savefig('demo01')
plt.show()