n, m = map(int, input().split())
card = []
result = 0

for _ in range(n):
    tmp = list(map(int, input().split()))
    min_value = 10001
    for a in tmp:
        min_value = min(a, min_value)
    result = max(min_value, result)


print(result)