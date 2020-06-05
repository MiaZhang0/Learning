# 1. 选择排序法
numbers = [8,0,9,4,7]
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i] > numbers[j]:
            # 快速交互
            numbers[i],numbers[j] = numbers[j],numbers[i]
print(numbers)

# 2. 冒泡排序法
for i in range(len(numbers)-1):
    # 每一轮的比较，注意range的变化，这里需要进行len(numbers)-1长的比较，注意-i意义(可以减少比较已经排好序的元素)
    for j in range(0,len(numbers)-1-i):
        if numbers[j] > numbers[j+1]:
            tmp = numbers[j]
            numbers[j] = numbers[j+1]
            numbers[j+1] = tmp
print(numbers)



