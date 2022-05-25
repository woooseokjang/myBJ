for i in range(int(input())):
    m, n, x, y = map(int, input().split())
    flag = True
    while x < m * n + 1:
        if x % n == y % n:
            print(x)
            flag = False
            break
        else:
            x = x + m
    if flag:
        print(-1)
