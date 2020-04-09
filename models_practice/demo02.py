#多元线性回归模型，相当于求多元函数的系数即向量。此处涉及线性代数矩阵、向量、秩、矩阵的逆、矩阵的转置
from sklearn import model_selection
import pandas as pd
import statsmodels.api as sm

#导入数据
path = r'E:\workspace\testdatas\Predict to Profit.xlsx'
Profit = pd.read_excel(path)
#将数据集拆分为训练集和测试集
train,test=model_selection.train_test_split(Profit,test_size=0.2,random_state=1234)
#根据train数据集建模
model = sm.formula.ols('Profit~RD_Spend+Administration+Marketing_Spend+C(State)',data=train).fit()

print('模型的偏回归系数分别为：\n',model.params)
#删除test数据集中的Profit变量，用剩下的自变量进行预测
test_X = test.drop(labels='Profit',axis=1)
pred = model.predict(exog=test_X)
print('对比预测值和实际值的差异：\n',pd.DataFrame({'Prediction':pred,'Real':test.Profit}))
print('*************************************************************************************')
#生成由State变量衍生的哑变量
dummies = pd.get_dummies(Profit.State)
#将哑变量与原始数据集水平合并
Profit_New = pd.concat([Profit,dummies],axis=1)
#删除State变量和California变量（因为State变量已被分解为哑变量，NewYork变量需要作为参照组）
Profit_New.drop(labels=['State','New York'],axis=1,inplace=True)
#拆分数据集Profit_New
train,test = model_selection.train_test_split(Profit_New,test_size=0.2,random_state=1234)
#建模
model2 = sm.formula.ols('Profit~RD_Spend+Administration+Marketing_Spend+Florida+California',data=train).fit()
print('模型的偏回归系数分别为：\n',model2.params)
print('*************************************************************************************')
# Profit与其余变量的相关系数
p1 = Profit.drop('State',axis=1).corrwith(Profit['Profit'])
print(p1)
print('*************************************************************************************')
# 变量两两相关的相关系数
p2 = Profit.drop('State',axis=1).corr()
print(p2)