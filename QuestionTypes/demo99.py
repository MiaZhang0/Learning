#对于9x9围棋盘，用a-i标识各行，用1-9标识各列，设计函数go()，输入位置和颜色，即输出文本棋盘，模拟围棋对弈的过程。
def print_go(phase):
    print('+-------------------+')
    for row in phase:
        print('| ',end='')
        for col in row:
            print('%s '%col,end='')
        print('|')
    print('+-------------------+')

def go(phase,pos,color):
    row = ord(pos[0]) - ord('a')
    col = int(pos[1]) - 1
    phase[row][col] = color
    print_go(phase)
    return phase

phase = [['-' for i in range(9)] for j in range(9)]
phase = go(phase,'c7','b')

phase = go(phase,'g3','w')

phase = go(phase,'g7','b')

phase = go(phase,'c3','w')

phase = go(phase,'e5','b')