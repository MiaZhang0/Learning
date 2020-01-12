#清除字符串‘\t python \n’左侧、右侧，以及左右两侧的空白字符。
s = '\t python \n'
res1 = s.lstrip()
print(res1)
res2 = s.rstrip()
print(res2)
res3 = s.strip()
print(res3)