# https://www.acmicpc.net/problem/2475
a, b, c, d, e = map(int, input().split())
print((a*a + b*b + c*c + d*d + e*e) % 10)
