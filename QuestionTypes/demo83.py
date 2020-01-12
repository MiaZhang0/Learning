# 找到列表[8,5,2,4,3,6,5,5,1,4,5]中出现最频繁的数字以及出现的次数
a = [8,5,2,4,3,6,5,5,1,4,5]
v_max = max(set(a),key=a.count)
print(v_max)
print(a.count(v_max))