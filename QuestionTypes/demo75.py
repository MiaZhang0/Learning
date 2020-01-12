#向csv_data.csv文件追加二维列表[[1.468,1.975,1.446],[1.718,1.826,1.359]]，然后读出所有数据。
with open(r'd:\csv_data.csv','a') as fp:
    for row in [[1.468,1.975,1.446],[1.718,1.826,1.359]]:
        line_len = fp.write('%s\n'%(','.join([str(col) for col in row])))

data = list()
with open(r'd:\csv_data.csv','r') as fp:
    for line in fp.readlines():
        data.append([float(item) for item in line.strip().split(',')])
print(data)