a = int(input())
b = int(input())
c = int(input())

mul = a * b * c

mul = list(str(mul))

arr = []
for i in range(10):
    arr.append(0)

for i in mul:
    arr[int(i)] = arr[int(i)] + 1

for i in arr:
    print(i)
