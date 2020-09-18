'''
2217번 : 로프
'''

n = int(input())
ropes = []
for _ in range(n):
    ropes.append(int(input()))

ropes.sort(reverse=True)

result = []

for i in range(n):
    result.append(ropes[i]*(i+1))



print(max(result))