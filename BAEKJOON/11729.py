result = []
def move(start, goal):
    result.append(f"{start} {goal}")

def hanoi(n, start, root, goal): # 재귀 과정
    # n은 갯수, start는 시작점, goal은 도착점, root는 거치는 점
    # start에서 root를 거쳐 goal로 가겠다
    if n == 1:
        move(start, goal)
    else:
        hanoi(n-1, start,goal,root)
        # 하나를 빼고(n-1) start에서 goal을 거쳐 root로 가겠다
        move(start,goal)
        # 하나(제일 큰 판)를 start에서 goal로 가겠다
        hanoi(n-1, root, start, goal)
        # 하나를 빼고(n-1) root에서 start를 거쳐 goal로 가겠다

hanoi_piece = int(input())

hanoi(hanoi_piece, "1", "2", "3")
print(len(result))
for i in result:
    print(i)