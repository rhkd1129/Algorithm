#자릿수의 합
import sys
#sys.stdin = open('input.txt', 'rt')
n = int(input())
arr = list(map(int, input().split()))

def digit_sum(x):
    sum = 0
    while True:
        sum += x%10
        x //= 10
        if x == 0:
            break
    return sum

max = 0
maxIndex = -1
sumArr = []
for i in range(n):
    tmp = digit_sum(arr[i])
    sumArr.append(tmp)
    if tmp > max:
        max = tmp
        maxIndex = i

print(arr[maxIndex])