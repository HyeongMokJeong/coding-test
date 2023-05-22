import sys; input = sys.stdin.readline

N, K = map(int, input().split())
if K < 5:
    print(0)
    exit()
elif K == 26:
    print(N)
    exit()
result = 0
words = [set(input().rstrip()) for _ in range(N)]
learn = [0] * 26
for i in ['a', 'c', 'i', 'n', 't']: learn[ord(i) - ord('a')] = 1

def dfs(idx, count):
    global result

    if count == K - 5:
        temp = 0
        for word in words:
            for i in word:
                if not learn[ord(i) - ord('a')]: break
            else: temp += 1
        result = max(result, temp)
        return

    for i in range(idx, 26):
        if not learn[i]:
            learn[i] = 1
            dfs(i, count + 1)
            learn[i] = 0
dfs(0, 0)
print(result)