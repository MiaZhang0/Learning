#从csv_data.csv文件中读出二维列表。
data = list()
with open(r'd:\csv_data.csv','r') as fp:
    for line in fp.readlines():
        data.append([float(item) for item in line.strip().split(',')])
print(data)