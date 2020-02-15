#     把浮点数分成证书和小数部分
#     num是


SIZE = 7
array = [[0] * SIZE]
for i in range(SIZE - 1):
    array += [[0] * SIZE]
# print(array)
j = 0
k = 0
orient = 0
for x in range(1, SIZE * SIZE + 1):
    array[j][k] = x
    if j + k == SIZE - 1:
        if j > k:
            orient = 1
        else:
            orient = 2
    elif (k == j) and (k >= SIZE/2):
        orient = 3
    elif (j == k - 1) and (k <= SIZE/2):
        orient = 0
    if orient == 0:
        j += 1
    elif orient == 1:
        k += 1
    elif orient == 2:
        k -= 1
    elif orient == 3:
        j -= 1
for i in range(SIZE):
    for j in range(SIZE):
        print('%02d ' % array[i][j], end="")
    print("")
