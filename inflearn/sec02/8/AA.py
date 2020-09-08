# 뒤집은 소수
import sys
#sys.stdin = open('input.txt', 'rt')
n = int(input())
arr = list(map(int, input().split()))

def reverse(x):
    str_x = str(x)
    tmp = ''
    for i in range(len(str_x)):
        tmp += str_x[len(str_x)-i-1]

    return int(tmp)

def isPrime(x):
    for i in range(2, x):
        if x%i==0:
            return False
    return True


for i in arr:
    tmp = reverse(i)
    if isPrime(tmp):
        print(tmp, end=' ')
