m, n = map(int, input().split())
arr = []
count = []

for i in range(m):
    arr.append(input())

for a in range(m-7):
    for b in range(n-7):
        cntW = 0
        cntB = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if(i+j) % 2 == 0:
                    if arr[i][j] == 'B':
                        cntW = cntW + 1
                    else:
                        cntB = cntB + 1
                else:
                    if arr[i][j] == 'B':
                        cntB = cntB + 1
                    else:
                        cntW = cntW + 1
        count.append(min(cntW, cntB))
print(min(count))
