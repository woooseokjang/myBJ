arr = [0 for _ in range(26)]
s = input()
s = list(s)
for c in s:
    arr[ord(c.upper()) - 65] = arr[ord(c.upper()) - 65] + 1
max = max(arr)
index = arr.index(max)
if len(list(filter(lambda i: arr[i] == max, range(len(arr))))) >= 2:
    print('?')
else:
    print(chr(index + 65))
