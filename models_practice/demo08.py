#SVM模型的应用
from sklearn import svm
import pandas as pd
from sklearn import model_selection
from sklearn import metrics
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import norm
from sklearn import preprocessing
import numpy as np
from sklearn import neighbors

# 读取外部数据
letters = pd.read_csv(r'E:\workspace\testdatas\letterdata.csv')
# 打印数据前5行
print(letters.head())
# 将数据拆分为训练集和测试集
predictors = letters.columns[1:]
X_train,X_test,y_train,y_test = model_selection.train_test_split(letters[predictors], letters.letter,
                                                                 test_size=0.25, random_state=1234)
# LinearSVC(C=1.0, class_weight=None, dual=True, fit_intercept=True,intercept_scaling=1, loss='squared_hinge', max_iter=1000,
# multi_class='ovr', penalty='l2', random_state=None, tol=0.0001,verbose=0)
# 选择线性可分SVM模型
linear_svc = svm.LinearSVC(C=1.0, class_weight=None, dual=True, fit_intercept=True,intercept_scaling=1, loss='squared_hinge',
                           max_iter=10000,multi_class='ovr', penalty='l2', random_state=None, tol=0.0001,verbose=0)
# 模型在训练数据集上的拟合
linear_svc.fit(X_train,y_train)
# 模型在测试集上的预测
pred_linear_svc = linear_svc.predict(X_test)
# 模型的预测准确率
metrics.accuracy_score(y_test, pred_linear_svc)
# 选择非线性SVM模型
nolinear_svc = svm.SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,decision_function_shape='ovr', degree=3,
                       gamma='auto',kernel='rbf',max_iter=-1, probability=False, random_state=None,
                       shrinking=True, tol=0.001, verbose=False)
# 模型在训练数据集上的拟合
nolinear_svc.fit(X_train,y_train)
# 模型在测试集上的预测
pred_svc = nolinear_svc.predict(X_test)
# 模型的预测准确率
metrics.accuracy_score(y_test,pred_svc)


# SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,decision_function_shape='ovr', degree=3, gamma='auto_deprecated',kernel='rbf',
#     max_iter=-1, probability=False, random_state=None,shrinking=True, tol=0.001, verbose=False)

# 读取外部数据
forestfires = pd.read_csv(r'E:\workspace\testdatas\forestfires.csv')
# 删除day变量
forestfires.drop('day',axis=1, inplace=True)
# 将月份作数值化处理
forestfires.month = pd.factorize(forestfires.month)[0]
# 绘制森林烧毁面积的直方图
sns.distplot(forestfires.area, bins=50, kde=True, fit=norm, hist_kws={'color':'steelblue'},
             kde_kws={'color':'red', 'label':'Kernel Density'},fit_kws={'color':'black','label':'Nomal', 'linestyle':'--'})
# 显示图例
plt.legend()
# 显示图形
plt.show()

# 对area变量作对数变换
y = np.log1p(forestfires.area)
# 将X变量作标准化处理
predictors = forestfires.columns[:-1]
X = preprocessing.scale(forestfires[predictors])
# 将数据拆分为训练集和测试集
X_train,X_test,y_train,y_test = model_selection.train_test_split(X, y, test_size=0.25, random_state=1234)
# 构建默认参数的SVM回归模型
svr = svm.SVR()
# 模型在训练数据集上的拟合
svr.fit(X_train,y_train)
# 模型在测试上的预测
pred_svr = svr.predict(X_test)
# 计算模型的MSE
mse1 = metrics.mean_squared_error(y_test,pred_svr)
print('模型的MSE:',mse1)
# 使用网格搜索法，选择SVM回归中的最佳C值、epsilon值和gamma值
epsilon = np.arange(0.1,1.5,0.2)
C= np.arange(100,1000,200)
gamma = np.arange(0.001,0.01,0.002)
parameters = {'epsilon':epsilon,'C':C,'gamma':gamma}
grid_svr = model_selection.GridSearchCV(estimator=svm.SVR(max_iter=10000),param_grid=parameters,
                                        scoring='neg_mean_squared_error',cv=5,verbose =1, n_jobs=2)
# 模型在训练数据集上的拟合
grid_svr.fit(X_train,y_train)
# 返回交叉验证后的最佳参数值
print('交叉验证后的最佳参数值:',grid_svr.best_params_, grid_svr.best_score_)
# 模型在测试集上的预测
pred_grid_svr = grid_svr.predict(X_test)
# 计算模型在测试集上的MSE值
mse2 = metrics.mean_squared_error(y_test,pred_grid_svr)
print('模型在测试集上的MSE值:',mse2)


