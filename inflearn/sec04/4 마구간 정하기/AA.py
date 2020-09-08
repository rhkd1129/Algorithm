# 마구간 정하기(결정 알고리즘)
import sys
sys.stdin = open('input.txt', 'rt')

def Count(distance):
    cnt = 1
    tmp = Line[0]
    for x in Line:
        if x - tmp >= distance:
            tmp = x
            cnt += 1
    return cnt

n, c= map(int, input().split())
Line = [int(input()) for _ in range(n)]
Line.sort()
lt = 1
rt = max(Line)
res = 0
while lt <= rt:
    mid = (lt+rt)//2
    if Count(mid) >= c:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)
