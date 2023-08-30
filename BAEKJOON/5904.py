import sys; sys.setrecursionlimit(10**9)
N = int(input())

def recur(leng, idx, n):
    temp = (leng - idx) // 2 # moo(k - 1)의 길이 ( moo(k - 1) / 가운데 / moo(k - 1))
    if n <= temp: return recur(temp, idx - 1, n) # 왼쪽 moo(k - 1)에 속한다면 moo(k - 1)에서 n번째 요소 찾기
    elif n > temp + idx: return recur(temp, idx - 1, n - temp - idx) # 오른쪽 moo(k - 1)에 속한다면 moo(k - 1)에서 n - moo(k - 1)의 길이 - 가운데 길이 번째 요소 찾기
    else: return "o" if n - temp - 1 else "m"
    # 가운데 속하고, n의 위치가 첫번째(1)이라면 인덱스는 0이므로 print m

leng, idx = 3, 0 # 전체 길이, 최대 N
while N > leng:
    idx += 1
    leng = leng * 2 + idx + 3

print(recur(leng, idx + 3, N)) # 전체 길이, 가운데 길이, N