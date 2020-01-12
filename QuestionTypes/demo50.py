#将字符串‘this is python’切片成3个单词
s = 'this is python'
#无参数，则默认使用空格切片，且自动忽略多余空格。若加上‘’做切片参数，会导致复杂结果
res1 = s.split()
print(res1)
res2 = s.split(' ')
print(res2)
