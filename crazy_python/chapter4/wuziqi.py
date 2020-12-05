import os

Board_Size = 15
# 二维列表棋盘
board = []


def initboard():
    for i in range(Board_Size):
        row = ['╋'] * Board_Size
        board.append(row)


# 输出棋盘
def pboard():
    for i in range(Board_Size):
        for j in range(Board_Size):
            # 打印不换行
            print(board[i][j], end='')
        print()


initboard()
pboard()

inputStr = input('请输入下棋的坐标，x,y形式 \n')
while inputStr is not None:
    x_str, y_str = inputStr.split(sep=',')
    board[int(y_str)-1][int(x_str)-1] = "●"
    pboard()
    inputStr = input('请输入下棋的坐标，x,y形式 \n')
    os.system('cls')


