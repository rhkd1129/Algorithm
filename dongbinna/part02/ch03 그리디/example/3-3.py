n, m = map(int, input().split())
card = []
result = 0

for _ in range(n):
    tmp = list(map(int, input().split()))
    min_value = min(tmp)
    result = max(min_value, result)



print(result)