import sys, queue

k = int(input())
w, h = map(int, input().split())
ary = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
dx2 = [-2, -1, 1, 2, -2, -1, 1, 2]
dy2 = [-1, -2, -2, -1, 1, 2, 2, 1]

q = queue.Queue()
q.put((0, 0, 0, 0)) # x, y, k count, all

def bfs():
    global result
    while q:
        t = q.get()
        if t[2] > k: continue
        if t[0] == w - 1 and t[1] == h - 1:
            return t[3]
        for i in range(4):
            dxx = t[0] + dx[i]
            dyy = t[1] + dy[i]
            if dxx < 0 or dxx >= w or dyy < 0 or dyy >= h: continue
            if ary[dxx][dyy] == 1:
                for j in range(8):
                    dxxx = t[0] + dx2[i]
                    dyyy = t[1] + dy2[i]
                    q.put((dxxx, dyyy, t[2] + 1, t[3] + 1))
            else:
                q.put((dxx, dyy, t[2], t[3] + 1))

print(bfs())