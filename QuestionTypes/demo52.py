#将字符串‘2.72,5,7,3.14’以半角逗号切片后，再将各个元素转成浮点型或整型
s = '2.72,5,7,3.14'
res = [float(item) if '.' in item else int(item) for item in s.split(',')]
print(res)