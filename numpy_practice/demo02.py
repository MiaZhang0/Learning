#赌局模拟，本钱1000，局数1500，每一局的输赢概率各为0.5
import numpy as np
import matplotlib.pyplot as plt

initial = 1000
package = [initial]
array = np.random.uniform(0,1,1500)
for time in array:
    if time < 0.5:
        initial -= 8
    else:
        initial += 8
    package.append(initial)

if initial < 1000:
    print('1500局之后剩余' + str(initial) + '输了' + str(1000-initial))
print(package)
#将结果画曲线图
plt.plot(range(1501),package)
plt.show()