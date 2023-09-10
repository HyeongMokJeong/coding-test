import sys; input = sys.stdin.readline
from collections import defaultdict

def run(w):
    if len(w) == len(word):
        print(w)
        return
    for i in visited:
        if visited[i]:
            visited[i] -= 1
            run(w + i)
            visited[i] += 1

for _ in range(int(input())):
    word = sorted(input().rstrip())
    visited = defaultdict(int)
    for i in word: visited[i] += 1
    run("")