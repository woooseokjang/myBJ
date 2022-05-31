from collections import Counter

n = int(input())
arr = [None for _ in range(8001)]
arr2 = []
sum = 0
for _ in range(n):
    i = int(input())
    sum = sum + i
    arr2.append(i)
    i = i + 4000
    if arr[i] == None:
        arr[i] = 0
    arr[i] = arr[i] + 1


print(round(sum / n))
arr2.sort()
print(arr2[len(arr2)//2])
cnt = Counter(arr)
most = cnt.most_common()
if most[0][0] == None:
    most = most[1:]
most.sort(key=lambda x: x[1])
most.reverse()
if most[0][1] == 1:
    print(arr.index(most[0][0]) - 4000)
else:
    arr3 = list(filter(lambda x: arr[x] == most[0][0], range(len(arr))))
    print(arr3[1] - 4000)
print(arr2[len(arr2) - 1] - arr2[0])
