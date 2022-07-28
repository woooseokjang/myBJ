from collections import Counter
import sys

n = int(sys.stdin.readline())
arr = []

for i in range(n):
    arr.append(int(sys.stdin.readline()))

print(round(sum(arr) / n))
arr.sort()
print(arr[int(i / 2)])
counter = Counter(arr).most_common()
if len(counter) > 1:
    if counter[0][1] == counter[1][1]:
        print(counter[1][0])
    else:
        print(counter[0][0])
else:
    print(counter[0][0])
print(arr[-1] - arr[0])
