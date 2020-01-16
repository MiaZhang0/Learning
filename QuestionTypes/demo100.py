#下图中是国际跳棋的初始局面，10x10的棋盘上只有50个深色格子可以落子，‘w’表示白色棋子，‘b’表示黑色棋子，‘-’表示无子，
# 字符串phase = ‘b’* 20 + ‘-’*10 + ‘w’*20 表示下图中的局面，请将phase打印成下图右所示的样子。

phase = 'b'*20 + '-'*10 + 'w'*20
def print_draughts(phase):
    print('+ - - - - - - - - - - +')
    for i in range(10):
        print('| ',end='')
        for j in range(10):
            if i%2 == 0 and j%2 or i%2 and j%2 == 0:
                print('%s '%phase[(10*i + j)//2],end='')
            else:
                print('- ',end='')
        print('|')
    print('+ - - - - - - - - - - +')
print_draughts(phase)