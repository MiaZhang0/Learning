# 绘制y = x的平方折线图
import numpy as np
import matplotlib.pyplot as plt

# x = np.arange(-5, 6, 1)
x = np.linspace(-5,5,10)
y = pow(x, 2)
# fig = plt.figure(figsize=(9, 5), dpi=100)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x,y)
# 绘制，属性设置
plt.plot(x, y, 'kh-.', label='$y=x^2$')
plt.legend(loc=9)
plt.title('$y=x^2$')
# 先保存再显示，不然图片结果为空白
plt.savefig('demo02')
plt.show()
