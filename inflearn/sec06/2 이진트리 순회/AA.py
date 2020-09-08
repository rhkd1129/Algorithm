# 이진트리 순회(깊이우선탐색)
import sys
sys.stdin=open('input.txt', 'rt')

def DFS(v):
    if v > 7:
        return
    else:
        # 전위 순회
        print(v, end=' ')
        DFS(v*2)
        # 중위 순회
        # print(v, end=' ')
        DFS(v*2+1)
        # 후위 순회
        # print(v, end=' ')

if __name__ == '__main__':
    DFS(1)