import random
# 1. name变量对应的值的前3个字符逆序输出
# name = 'ZhangXiaoMei'
# print(name[2::-1])

# 2. 开发敏感词语过滤程序，提示用户输入内容，如果用户输入的内容中包含特殊的字符：如“苍老师”，“东京热”，则将内容替换为***
# s = input('请输入内容：')
# word = ['苍老师','东京热']
# for i in word:
#     if i in s:
#         s = s.replace(i,'***')
# print(s)

'''
3. 循环提示用户输入：用户名、密码、邮箱（要求用户输入的长度不超过20个字符，如果超过则只有前20个字符有效）
打印输出
用户名   密码   邮箱
Admin    123    hfjs@163.com
Lily     111    yweuyr@163.com
····
如果用户输入 q 或 Q 表示不再继续输入。
'''
# s = ''
# while True:
#     print('请依次您的输入用户名、密码、邮箱（长度不超过20个字符，如果超过则只有前20个字符有效）。输入q或Q表示结束')
#     username = input('请输入用户名：')
#     if ('q' in username) or ('Q' in username):
#         break
#     username = username[0:20]
#     password = input('请输入密码：')
#     if ('q' in password) or ('Q' in password):
#         break
#     password = password[0:20]
#     email = input('请输入邮箱：')
#     if ('q' in email) or ('Q' in email):
#         break
#     email = email[0:20]
#     message = '{}\t{}\t{}\n'.format(username,password,email)
#     # message = message.expandtabs(20)
#     s += message
#     print(s)

# 4. 执行程序产生验证码，提示用户输入用户名，密码和验证码，如果正确，则提示登录成功，否则重新输入。（要求产生新的验证码）
# username = input('请输入用户名：')
# password = input('请输入密码：')
# while True:
#     str = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890'
#     s = ''
#     for i in range(4):
#         index = random.randint(0,len(str)-1)
#         s += str[index]
#     print(s)
#     code = input('请输入验证码：')
#     if code.lower() == s.lower():
#         print('登录成功')
#         break
#     else:
#         print('验证码错误，请重新输入')

# 5. 输入一行字符，统计其中有多少个单词，每两个单词之间以空格隔开
s = 'hello Amy I am fine and you I am OK'
result = s.split(' ')
print(result)
n = s.count(' ')
print(n)
result1 = s.split(' ',2)

str = 'hdsjuhfiedlfierwoqe948147hfdncxkz,kdslafidjfavnhfdvf.dkcvmfdkfdgregtrfehswt'
print(str.count(''))
list = []
for i in range(0,len(str),2):
    list.append(str[i:i+2])
print(' '.join(list))


# 6. 输入两个字符串，从第一字符串中删除第二个字符串中所有的字符。例如，输入“They are students.” 和“aeiou”,则删除之后的第一个字符串变成“Thy r stdnts.”
# s1 = input('请输入第一个字符串：')
# s2 = input('请输入第二个字符串：')
# for i in s2:
#     s1 = s1.replace(i,'')
# print(s1)

'''
7. 小易喜欢的单词具有以下特性：（1）单词每个字母都是大写字母；（2）单词没有连续相等的字母
例如：
小易不喜欢“ABBA”，因为这里面有两个连续的‘B’
小易喜欢‘A’，‘ABA’和‘ABCBA’这些单词
给你一个单词，你要回答小易是否会喜欢这个单词。
'''
# word = input('请输入单词：')
# for i in range(len(word)):
#     if word[i] < 'A' or word[i] > 'Z':
#         print('不喜欢')
#         break
#     else:
#         if i < len(word)-1 and word[i] == word[i+1]:
#             print('不喜欢')
#             break
# else:
#     print('喜欢')
