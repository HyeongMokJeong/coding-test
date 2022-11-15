import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

card = [str(int(sys.stdin.readline())) for _ in range(n)]
idxs = []
result = []

def make(idx):
    if len(idx) == k:
        idxs.append(tuple(idx))
        return
    
    for i in range(len(card)):
        if i not in idx:
            idx.append(i)
            make(idx)
            idx.pop()

make([])

for i in idxs:
    tmp = ""
    for j in i:
        tmp += card[j]
    if tmp not in result:
        result.append(tmp)

print(len(result))