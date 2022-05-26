# https://www.acmicpc.net/problem/1181
n = int(input())
arr = []
for i in range(n):
    arr.append(input())
arr = set(arr)
arr = list(arr)
arr.sort()
arr.sort(key=len)
for item in arr:
    print(item)
