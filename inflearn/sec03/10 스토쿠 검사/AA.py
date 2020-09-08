# 스토쿠 검사
import sys
sys.stdin = open('input.txt', 'rt')
arr = []
for i in range(9):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

flag = True

for i in range(9):
    tmp = set()
    for j in range(9):
        tmp.add(arr[i][j])
    if len(tmp) != 9:
        flag = False

for i in range(9):
    tmp = set()
    for j in range(9):
        tmp.add(arr[j][i])
    if len(tmp) != 9:
        flag = False

for i in range(0, 7, 3):
    for j in range(0, 7, 3):
        tmp = set()
        for x in range(i, i+3):
            for y in range(j, j+3):

                tmp.add(arr[x][y])
        if len(tmp) != 9:
            flag = False

if flag:
    print('YES')
else:
    print('NO')


