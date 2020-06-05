# 正则表达式
import re
'''
基础
. 任意字符
[] 范围
| 或者
() 一组

量词
* >=0
+ >=1
? 0,1
{m} =m
{m,} >=m
{m,n} >=m <=n

预定义
\s space(空格)
\S not space
\d digit(数字)
\D not digit
\w word [0-9a-zA-Z]
\W not word [^0-9a-zA-Z]

分组
() group()
number 对称引用
name   对称对很多时，起名引用
'''
pattern = re.compile('要查询的字符')
pattern.match('信息源')  # 表示与开头开始搜索匹配
r = pattern.search('信息源')  # 在整个‘信息源’中搜索匹配
# r.span() # 获取‘要查询的字符’的位置
# r.group() # 提取到匹配的内容
# r.groups()
msg = 'dsefre8793737hdfhdl45g56t9'
result = re.search('[a-z][0-9][a-z]', msg)  # 只会匹配到信息源中的第一个，后面不会继续进行检索
re.findall('[a-z][0-9][a-z]', msg)  # findall 匹配整个字符串，找出所有的要查询的字符
# 用正则表达式验证qq号码5~11位，开头不是0
qq = '102938274'
# {m,n}从m次到n次；'^ $'从^开始，$结束
result1 = re.match('^[1-9][0-9]{4,10}$', qq)
print(result1)
# 用户名是字母或数字，不能是数字开头，用户名长度必须6位以上
username = 'admin398'
result2 = re.match('[a-zA-z][0-9a-zA-Z]{5,}', username)
print(result2)
# 用户名是字母或数字或者下划线，不能是数字开头，用户名长度必须6位以上 \w 等价于[0-9a-zA-Z_]
result3 = re.match('[a-zA-z]\w{5,}', username)
# 手机号码正则验证
phone = ''
re.match('1[35789]\d{9}$', phone)
# 邮箱验证163，126,qq
email = ''
re.match(r'\w(5,20)@(163|126|qq)\.(com|cn)$',email)
# 分组提取，（）表示分组
tel = '010-12345678'
tel_result = re.match(r'(\d{3}|\d{4})-(\d{8})$',tel)
# print(tel_result.group())
# print(tel_result.group(1))
# print(tel_result.group(2))
# 分组引用，加number
message1 = '<html><h1>abc</h1>'
message2 = '<h1>hello</h1>'
message3 = '<html><h1>abc</h1></html>'
result5 = re.match(r'<([0-9a-zA-Z]+)>(.+)</([0-9a-zA-Z]+)>$',message1)
print(result5)
result4 = re.match(r'<([0-9a-zA-Z]+)>(.+)</\1>$',message2)
print(result4)
print(result4.group(2))
result6 = re.match(r'<([0-9a-zA-Z]+)><([0-9a-zA-Z]+)>(.+)</\2></\1>$',message3)
print(result6)
# 起名的方式： （？P<名字>正则） （？P=名字）
result7 = re.match(r'<(?P<name1>\w+)><?P<name2>\w+>(.+)</(?P=name2)><(?P=name1)>',message3)
# re.sub(正则表达式，‘新内容’(可以是函数)，string) 替换
# re.split(r'[,:]',string) 将string按逗号和冒号分割（可以按多种符号切割）
'''python中数量词默认是贪婪的（在少数语言里也可能是默认非贪婪），总是尝试匹配尽可能多的字符
非贪婪相反，总是尝试匹配尽可能少的字符
在* ，？，+，{m,n}后面加上？，使贪婪变成非贪婪
'''