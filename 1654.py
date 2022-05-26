# https://www.acmicpc.net/problem/1654
import sys


k, n = map(int, input().split())
lan = []
for i in range(k):
    lan.append(int(input()))

min = 1
max = max(lan)
while min <= max:
    mid = (min + max) // 2
    cnt = 0
    for i in lan:
        cnt = cnt + i // mid
    if cnt >= n:
        min = mid + 1
    else:
        max = mid - 1
print(max)
