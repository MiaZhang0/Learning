#判断字符串‘adS12K56’是否完全为字母数字，是否全为数字，是否全为字母，是否全为ASCII码。
s = 'adS12K56'
res1 = s.isalnum()
print(res1)
res2 = s.isdigit()
print(res2)
res3 = s.isascii()
print(res3)