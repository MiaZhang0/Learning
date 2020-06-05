# 添加元素
# 用户注册功能，字典的应用
print('*'*30,'欢迎来到kedalo用户注册系统','*'*30)
# 模拟数据库
database = []
while True:
    # 定义一个字典
    users = {}
    username = input('请输入用户名：')
    password = input('请输入密码：')
    repassword = input('请再次输入密码：')
    if password ==repassword:
        users['password'] = password
    else:
        print('两次密码不一致,请重新输入')
        continue
    email = input('请输入邮箱：')
    phone = input('请输入手机号：')
    # 将信息保存到字典中
    users['username'] = username
    users['email'] = email
    users['phone'] = phone
    # 将注册信息保存到数据库列表中
    database.append(users)
    answer = input('是否继续注册？（y/n）')
    if answer != 'y':
        break
print(database)

# 查询元素:字典根据key获取value值
# items()，values()取出字典中的所有值，keys()取出字典中的所有键； 返回的全是列表
dict = {'Amy':88,'Tom':79,'Tim':96}
for i in dict:
    print(i)
print(dict.items())
print(dict.values())
print(dict.keys())

# 考试分数大于90分的人
for key,value in dict.items():
    if value > 90:
        print(key)
# 求所有学生的考试成绩平均分
for score in dict.values():
    print(score)
score = dict.values()
total = sum(score)
avg = total/len(score)
print(avg)
# 查询某个key是否在字典中，如果在，获取相应value；如果不存在，则返回默认值
# get(key)如果不存在，则返回None
# get(key,default)如果不存在，则返回默认值
# print(dict.get('Lily',80))

# 删除元素
del dict['Amy']
print(dict)
dict.pop('Tim')
# dict.popitem():删除末尾元素
# dict.clear():清空字典
print(dict)
