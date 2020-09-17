'''
11399번 : ATM
'''
n = int(input())
p = list(map(int, input().split()))
p.sort()
result = 0
for i in range(n):
    tmp = p[:i+1]
    result += sum(tmp)

print(result)

'''
a = int(input())
l = []
total = 0
cur = 0
l = list(map(int, input().split()))

l.sort()
for x in l:
    cur += x
    total += cur
print(total)
'''