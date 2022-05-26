import sys
sys.setrecursionlimit(10**6)


def binary(a, arr, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if a == arr[mid]:
        return 1
    elif a < arr[mid]:
        return binary(a, arr, start, mid - 1)
    else:
        return binary(a, arr, mid + 1, end)


n = int(input())
arr = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

arr.sort()

for a in arr2:
    res = binary(a, arr, 0, n - 1)
    print(res)
