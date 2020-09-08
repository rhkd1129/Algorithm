#k번째 큰 수
import sys
sys.stdin = open('input.txt', 'rt')
n = int(input())
a = list(map(int, input().split()))
avg = round(sum(a)/n)
min=2147000000
for index, value in enumerate(a):
    tmp = abs(value-avg)
    if tmp < min:
        min = tmp
        score = value
        res = index + 1
    elif tmp==min:
        if value > score:
            score = value
            res = index + 1
print(avg, res)


#
a=66.5
a=a+0.5
a=int(a)
print(a)