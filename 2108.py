n = int(input())
arr = [0 for _ in range(8001)]
arr2 = []
arr3 = []
sum = 0
for _ in range(n):
    i = int(input())
    sum = sum + i
    arr2.append(i)
    i = i + 4000
    arr[i] = arr[i] + 1


print("{:.0f}".format(sum / n))
arr2.sort()
print(arr2[len(arr2)//2])

max = 0
index = -1

for i in range(8001):
    if max == 0 and arr[i] > max:
        max = arr[i]
        index = i
    elif max != 0 and arr[i] > max:
        arr3.append([max, index])
        max = arr[i]
        index = i
    elif max != 0 and arr[i] == max:

max = arr.index(max(arr))
print(max)


print(arr2[len(arr2) - 1] - arr2[0])
