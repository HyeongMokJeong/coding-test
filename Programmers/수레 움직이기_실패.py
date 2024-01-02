def solution(maze):
    answer = float('inf')
    x, y = len(maze[0]), len(maze)
    for i in range(y):
        for j in range(x):
            if maze[i][j] == 1: red_s = (i, j)
            elif maze[i][j] == 2: blue_s = (i, j)
            elif maze[i][j] == 3: red_e = (i, j)
            elif maze[i][j] == 4: bule_e = (i, j)
    
    visited_r, visited_b = [[0] * x for _ in range(y)], [[0] * x for _ in range(y)]
    visited_r[red_s[0]][red_s[1]] = 1
    visited_b[blue_s[0]][blue_s[1]] = 1

    def dfs(red_c, blue_c, count):
        global answer
        if red_c == red_e and blue_c == bule_e:
            answer = min(answer, count)
            return
        
        rx, ry = red_c
        bx, by = blue_c

        for nrx, nry in [(rx + 1, ry), (rx - 1, ry), (rx, ry + 1), (rx, ry - 1)]:
            if 0 <= nrx < y and 0 <= nry < x and not visited_r[nrx][nry] and maze[nrx][nry] != 5:
                visited_r[nrx][nry] = 1

                for nbx, nby in [(bx + 1, by), (bx - 1, by), (bx, by + 1), (bx, by - 1)]:
                    if 0 <= nbx < y and 0 <= nby < x and not visited_b[nbx][nby] and (nrx != nbx and nry != nby) and (red_c != (nbx, nby) and blue_c != (nrx, nry)):
                        visited_b[nbx][nby] = 1
                        dfs((nrx, nry), (nbx, nby), count + 1) 
                visited_r[nrx][nry] = 0
    dfs(red_s, blue_s, 0)
    return 0 if answer == float('inf') else answer

print(solution([[1, 4], [0, 0], [2, 3]]))