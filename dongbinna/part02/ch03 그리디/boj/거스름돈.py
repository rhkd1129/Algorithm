'''
5585번 : 거스름돈
'''
n = int(input())
coins = [1, 5, 10, 50, 100, 500]
chage = 1000 - n
cnt = 0

while chage > 0:
    coin = coins.pop()
    cnt += chage//coin
    chage %= coin

print(cnt)