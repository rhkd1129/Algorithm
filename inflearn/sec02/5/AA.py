#정다면체
import sys
#sys.stdin = open('input.txt', 'rt')
n, m = map(int, input().split())
arr = []
for i in range(33):
    arr.append(0)

for i in range(1, n+1):
    for j in range(1, m+1):
        tmp = i + j
        arr[tmp] += 1

cnt = []
for i in range(len(arr)):
    if arr[i] == max(arr):
        cnt.append(i)

for i in range(len(cnt)):
    print(cnt[i], end=' ')