
def min(a, b):
    if a < b:
        return a
    return b


n = int(input())
arr = [[0 for row in range(3)] for cal in range(n)]

for i in range(n):
    a, b, c = input().split()
    arr[i][0] = int(a)
    arr[i][1] = int(b)
    arr[i][2] = int(c)

for i in range(1, n):
    arr[i][0] = min(arr[i-1][1], arr[i-1][2]) + arr[i][0]
    arr[i][1] = min(arr[i-1][0], arr[i-1][2]) + arr[i][1]
    arr[i][2] = min(arr[i-1][0], arr[i-1][1]) + arr[i][2]


print(min(min(arr[n-1][0], arr[n-1][1]), arr[n-1][2]))
