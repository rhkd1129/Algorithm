'''
2839번: 설탕 배달
'''
n = int(input())
cnt = 0
while n != 0:
    if n%5==0:
        cnt += n//5
        break

    n -= 3
    cnt += 1
    if n < 0:
        cnt = - 1
        break



print(cnt)