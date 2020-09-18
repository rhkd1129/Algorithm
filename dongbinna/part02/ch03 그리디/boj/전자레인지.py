'''
10162번 : 전자레인지
'''
t = int(input())
button = [300, 60, 10]
cnt = [0] * 3

for i in range(3):
    cnt[i] = t//button[i]
    t %= button[i]


if t == 0:
    for i in cnt:
        print(i, end=' ')
else:
    print(-1)
