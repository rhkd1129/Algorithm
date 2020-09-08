# 단어 찾기(해쉬)
import sys
sys.stdin = open('input.txt', 'rt')
n = int(input())
word = []
poem = []
for _ in range(n):
    word.append(input())

for _ in range(n-1):
    poem.append(input())

for x in word:
    if x not in poem:
        print(x)