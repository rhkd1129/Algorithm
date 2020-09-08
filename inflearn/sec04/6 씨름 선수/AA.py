# 씨름 선수 (그리디)
import sys
sys.stdin = open('input.txt', 'rt')
n = int(input())
player = []
for i in range(n):
    h, w = map(int, input().split())
    player.append((h, w))

player.sort(reverse=True)

max = 0
cnt = 0
for h, w in player:
    if w > max:
        max = w
        cnt += 1

print(cnt)