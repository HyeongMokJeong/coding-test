import sys

n = int(sys.stdin.readline().rstrip())
dic = dict()

for _ in range(n):
    a, b, c = list(sys.stdin.readline().split())
    dic[a] = [b, c]

def preorder(node):
    if node == '.': return
    a, b = dic[node]
    print(node, end='')
    preorder(a)
    preorder(b)


def inorder(node):
    if node == '.': return
    a, b = dic[node]
    inorder(a)
    print(node, end='')
    inorder(b)

def postorder(node):
    if node == '.': return
    a, b = dic[node]
    postorder(a)
    postorder(b)
    print(node, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')