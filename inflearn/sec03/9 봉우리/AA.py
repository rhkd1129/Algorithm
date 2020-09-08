#
import sys
# sys.stdin = open('input.txt', 'rt')
n = int(input())
arr = []

for i in range(n+2):
    tmp = [0] * (n+2)
    arr.append(tmp)

for i in range(n):
    tmp = list(map(int, input().split()))

    for j in range(1, n+1):
        arr[i+1][j] = tmp[j-1]


cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if arr[i][j] > arr[i][j-1] and arr[i][j] > arr[i][j+1] and arr[i][j] > arr[i+1][j] and arr[i][j] > arr[i-1][j]:
            cnt += 1
print(cnt)