# 역수열(그리디)
import sys
sys.stdin = open('input.txt', 'rt')
n = int(input())
a = list(map(int, input().split()))
seq = [0]*n

for i in range(1, n+1):
    cnt = 0
    for j in range(n):
        if cnt == a[i-1]:
            if seq[j] == 0:
                seq[j] = i
            else:
                continue
            break
        if seq[j] == 0:
            cnt += 1

for x in seq:
    print(x, end=' ')
