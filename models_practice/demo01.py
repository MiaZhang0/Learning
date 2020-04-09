#线性回归模型：一元线性回归模型,相当于求一元函数的系数与截距
import pandas as pd
import statsmodels.api as sm

path = r'E:\workspace\testdatas\Salary_Data.csv'
data = pd.read_csv(path)
#利用收入数据集，构建回归模型
fit = sm.formula.ols('Salary~YearsExperience',data=data).fit()
#返回模型的参数值
res = fit.params
print(res)

p= data.Salary.corr(data.YearsExperience)
print(p)