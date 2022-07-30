# https://www.acmicpc.net/problem/1074

n, r, c = map(int, input().split())

ans = 0

while n != 0:

    n -= 1
    border = pow(2, n)

    if r < border and c < border:
        None
    elif r < border and c >= border:
        c -= border
        ans += border * border
    elif r >= border and c < border:
        r -= border
        ans += border * border * 2
    elif r >= border and c >= border:
        c -= border
        r -= border
        ans += border * border * 3

print(ans)
