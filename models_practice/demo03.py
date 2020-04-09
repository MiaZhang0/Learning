#岭回归模型和Lasso回归模型，糖尿病数据的预测，解决矩阵不可逆的情况
import pandas as pd
import numpy as np
from sklearn import model_selection
from sklearn.linear_model import Ridge,RidgeCV
from sklearn.linear_model import Lasso,LassoCV
from sklearn.metrics import mean_squared_error
from statsmodels import api as sms

#读取糖尿病数据集
path = r'E:\workspace\testdatas\diabetes.xlsx'
diabetes = pd.read_excel(path)
#构造自变量（删除患者性别、年龄和因变量）
predictors = diabetes.columns[2:-1]
#将数据集拆分为训练集和测试集
X_train, X_test, y_train, y_test = model_selection.train_test_split(diabetes[predictors], diabetes['Y'], test_size=0.2, random_state=1234)
#构造不同的lambda值，等比数列，初始值是-5，结束值是2，构造200个lambda
lambdas = np.logspace(-5,2,200)
#设置交叉验证的参数，对于每一个lambda值，都执行10重交叉验证
ridge_cv = RidgeCV(alphas=lambdas, normalize=True, scoring='neg_mean_squared_error', cv=10)
#模拟拟合
ridge_cv.fit(X_train,y_train)
#返回最佳的lambda值
ridge_best_lambda = ridge_cv.alpha_
print(ridge_best_lambda)

#基于最佳的Lambda值建模
ridge = Ridge(alpha=ridge_best_lambda, normalize=True)
ridge.fit(X_train,y_train)
# 返回岭回归系数
ridge_coefficient = pd.Series(index=['Intercept'] + X_train.columns.tolist(), data=[ridge.intercept_] + ridge.coef_.tolist())
print(ridge_coefficient)
# 预测
ridge_predict = ridge.predict(X_test)
# 预测效果验证
ridge_RMSE = np.sqrt(mean_squared_error(y_test,ridge_predict))
print(ridge_RMSE)
print('********************************************')
# LASSO回归模型的交叉验证
lasso_cv = LassoCV(alphas=lambdas, normalize=True, cv=10, max_iter=10000)
lasso_cv.fit(X_train, y_train)
# 输出最佳的lambda值
lasso_best_alpha = lasso_cv.alpha_
print(lasso_best_alpha)
# 基于最佳的lambda值建模
lasso = Lasso(alpha = lasso_best_alpha, normalize=True, max_iter=10000)
lasso.fit(X_train, y_train)
# 返回LASSO回归的系数
lasso_coefficient = pd.Series(index = ['Intercept'] + X_train.columns.tolist(),data = [lasso.intercept_] + lasso.coef_.tolist())
print(lasso_coefficient)
# 预测
lasso_predict = lasso.predict(X_test)
# 预测效果验证
lasso_RMSE = np.sqrt(mean_squared_error(y_test,lasso_predict))
print(lasso_RMSE)
print('*****************************************')
# 为自变量X添加常数列1，用于拟合截距项
X_train2 = sms.add_constant(X_train)
X_test2 = sms.add_constant(X_test)
# 构建多元线性回归模型
linear = sms.OLS(y_train, X_train2).fit()
# 返回线性回归模型的系数
linear_coefficient = linear.params
print(linear_coefficient)
# 模型的预测
linear_predict = linear.predict(X_test2)
# 预测效果验证
linear_RMSE = np.sqrt(mean_squared_error(y_test,linear_predict))
print(linear_RMSE)
#备注：RMSE值越小越好，lasso_RMSE < ridge_RMSE < linear_RMSE