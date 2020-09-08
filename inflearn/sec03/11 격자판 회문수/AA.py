# 격자판 회문수
import sys
sys.stdin = open('input.txt', 'rt')
arr = []
for i in range(7):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

def check(x):
    if x[0] == x[-1] and x[1] == x[-2]:
        return True

cnt = 0

for i in range(7):
    for j in range(3):
        num = ''
        for x in range(j, j+5):
            num += str(arr[i][x])
        if check(num):
            cnt += 1

for i in range(7):
    for j in range(3):
        num = ''
        for x in range(j, j+5):
            num += str(arr[x][i])
        if check(num):
            cnt += 1

print(cnt)

