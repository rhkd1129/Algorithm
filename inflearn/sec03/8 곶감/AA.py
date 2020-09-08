# 곶감 (모래 시계)
import sys
sys.stdin = open('input.txt', 'rt')
n = int(input())
arr = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

m = int(input())
for i in range(m):
    a, b, c = list(map(int, input().split()))
    tmp = list(arr[a - 1])
    if b == 0:
        for j in range(n):
            arr[a-1][j-c] = tmp[j]
    if b == 1:
        for j in range(n):
            arr[a - 1][j-n+c] = tmp[j]

sum = 0

for i in range(n):
    if i <= n//2:
        for j in range(i, n-i):
            sum += arr[i][j]

    if i > n//2:
        for j in range(n-i-1, i + 1):
            sum += arr[i][j]

print(sum)