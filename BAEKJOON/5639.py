import sys
sys.setrecursionlimit(10**9)

tree = []
while 1:
    try:
        node = int(sys.stdin.readline().rstrip())
        tree.append(node)
    except: break

def postorder(s, e):
    if s > e: return

    m = e + 1
    for i in range(s + 1, e + 1):
        if tree[s] < tree[i]:
            m = i
            break
    
    postorder(s + 1, m - 1)
    postorder(m, e)
    print(tree[s])

postorder(0, len(tree) - 1)