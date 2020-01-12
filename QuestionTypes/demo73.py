#将二维列表[[0.468,0.975,0.446],[0.718,0.826,0.359]]写成名为csv_data的csv格式的文件，并尝试用Excel打开它
with open(r'd:\csv_data.csv','w') as fp:
    for row in [[0.468,0.975,0.446],[0.718,0.826,0.359]]:
        line_len = fp.write('%s\n'%(','.join([str(col) for col in row])))