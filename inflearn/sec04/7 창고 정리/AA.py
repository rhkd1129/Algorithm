# 창고 정리
import sys
sys.stdin = open('input.txt', 'rt')
l = int(input())
box = list(map(int, input().split()))
m = int(input())

for i in range(m):
    box.sort()
    box[0] += 1
    box[l-1] -= 1

print(max(box) - min(box))

