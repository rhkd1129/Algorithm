n = int(input())
data = list(map(int, input().split()))
result = 0
count = 0
data.sort()
for a in data:
    count += 1
    if count >= a:
        result += 1
        count = 0
print(result)