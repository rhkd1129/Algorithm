'''
1946번 : 신입 사원
'''
t = int(input())
for i in range(t):
    n = int(input())
    tmp = []
    for j in range(n):
        tmp.append(list(map(int, input().split())))
    tmp.sort()
    print(tmp)