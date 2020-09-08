import sys
sys.stdin=open('input.txt', 'rt')
# n = int(input())
# a = list(map(int, input().split()))
# seq = [0]*n
# for i in range(n):
#     for j in range(n):
#         if a[i] == 0 and seq[j]== 0:
#             seq[j] = i+1
#             break
#         elif seq[j] == 0:
#             a[i] -= 1
#
# for x in seq:
#     print(x, end=' ')

n = int(input())
a =list(map(int,input().split()))
a = a[::-1]
ans=[]
for x in a:
        ans.insert(x,n)
        n -=1

print(ans)
