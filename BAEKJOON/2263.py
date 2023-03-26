import sys
sys.setrecursionlimit(10 ** 5)

n = int(sys.stdin.readline().rstrip())
inorder = list(map(int, sys.stdin.readline().split()))
postorder = list(map(int, sys.stdin.readline().split()))
idxAry = [0] * (n + 1)
for i in range(n):
    idxAry[inorder[i]] = i # inorder 인덱스 저장

def recur(inStart, inEnd, postStart, postEnd):
    if inStart > inEnd or postStart > postEnd: return

    root = postorder[postEnd]
    print(root, end=" ")

    left = idxAry[root] - inStart # 왼쪽 서브트리의 노드 개수
    right = inEnd - idxAry[root] # 오른쪽 서브트리의 노드 개수

    recur(inStart, inStart + left - 1, postStart, postStart + left - 1)
    recur(inEnd - right + 1, inEnd, postEnd - right, postEnd - 1)


recur(0, n - 1, 0, n - 1)