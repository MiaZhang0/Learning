#数据的合并与连接
import pandas as pd

#构造数据集df1和df2
df1 = pd.DataFrame({'name':['张三','李四','王二'],'age':[21,25,22],'gender':['男','女','男']})
# print(df1)
df2 = pd.DataFrame({'name':['丁一','赵五'],'age':[23,22],'gender':['女','女']})
# print(df2)
#concat行合并，数据源的变量名称完全相同（变量名顺序没有要求）
#数据集的横向合并
result = pd.concat([df1,df2],keys=['df1','df2']).reset_index().drop(labels='level_1',axis=1).rename(columns={'level_0':'class'})
print(result)
#数据集的纵向合并
# print(pd.concat([df1,df2]))

print('********************************************')
#构造数据集
df3 = pd.DataFrame({'id':[1,2,3,4,5],'name':['张三','李四','王二','丁一','赵五'],'age':[27,24,25,23,25],'gender':['男','男','男','女','女']})
df4 = pd.DataFrame({'Id':[1,2,2,4,4,4,5],'score':[83,81,87,75,86,74,88],'subject':['科目1','科目1','科目2','科目1','科目2','科目3','科目1']})
df5 = pd.DataFrame({'id':[1,3,5],'name':['张三','王二','赵五'],'income':[13500,18000,15000]})

# print(df3)
# print(df4)
# print(df5)

#df3和df4先连接
mergel = pd.merge(left=df3,right=df4,how='left',left_on='id',right_on='Id')
print(mergel)
#将df5与merge1连接
merge2 = pd.merge(left=mergel,right=df5,how='left')
print(merge2)