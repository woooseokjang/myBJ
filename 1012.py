# https://www.acmicpc.net/problem/1012
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = [[x, y]]
    while q:
        a, b = q.pop()
        for i in range(4):
            a2 = a + dx[i]
            b2 = b + dy[i]
            if 0 <= a2 < n and 0 <= b2 < m and arr[a2][b2] == 1:
                arr[a2][b2] = 0
                q.append([a2, b2])


t = int(input())

for case in range(t):
    m, n, k = map(int, input().split())
    arr = [[0 for _ in range(m)] for _ in range(n)]
    cnt = 0
    for i in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                bfs(i, j)
                arr[i][j] = 0
                cnt = cnt + 1
    print(cnt)
