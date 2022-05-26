# https://www.acmicpc.net/problem/1003
zero = [1, 0, 1]
one = [0, 1, 1]

t = int(input())
arr = []
for _ in range(t):
    arr.append(int(input()))
for num in arr:
    length = len(zero)
    if num >= length:
        for i in range(length, num+1):
            zero.append(zero[i-1] + zero[i - 2])
            one.append(one[i-1] + one[i-2])
    print(zero[num], one[num])
