'''
11047번 : 동전 0
'''
n, k = map(int, input().split())
coins = []
cnt = 0
for _ in range(n):
    tmp = int(input())
    coins.append(tmp)

coins.sort(reverse=True)

for coin in coins:
    if coin > k:
        continue
    cnt += k//coin
    k %= coin
    if k == 0:
        break

print(cnt)