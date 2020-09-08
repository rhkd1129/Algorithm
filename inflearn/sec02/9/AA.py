#주사위 게임
import sys
#sys.stdin = open('input.txt', 'rt')
n = int(input())
a = []
for i in range(n):
    b = list(map(int, input().split()))
    a.append(b)

def countPrize(a):
    prize = 0
    if a[0] == a[1] and a[1] == a[2]:
        prize = 10000 + a[0]*1000
    elif a[0] == a[1]:
        prize = 1000 + a[0]*100
    elif a[1] == a[2]:
        prize = 1000 + a[1]*100
    elif a[0] == a[2]:
        prize = 1000 + a[0]*100
    else:
        prize = max(a)*100

    return prize

maxPrize = 0
maxIndex = -1
for i in range(len(a)):
    prize = countPrize(a[i])
    if prize > maxPrize:
        maxPrize = prize
        maxIndex = i

print(countPrize(a[maxIndex]))

