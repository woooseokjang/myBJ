t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    arr = []
    arr2 = []
    arr = list(map(int, input().split()))
    for j in range(n):
        arr2.append([arr[j], j])
    j = 1
    while True:
        now = arr2.pop(0)
        if not arr2:
            print(j)
            break
        if max(arr2)[0] > now[0]:
            arr2.append(now)
        else:
            if now[1] == m:
                print(j)
                break
            j = j + 1
