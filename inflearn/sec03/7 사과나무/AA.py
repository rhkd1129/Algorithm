# 사과나무
import sys
sys.stdin = open('input.txt', 'rt')
n = int(input())
arr = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)
sum = 0
for i in range(n):
    if i <= n//2:
        for j in range(n//2-i, n//2+1+i):
            sum += arr[i][j]

    if i > n//2:
        new_i = n - i - 1
        for j in range(n // 2 - new_i, n // 2 + 1 + new_i):
            sum += arr[i][j]

print(sum)