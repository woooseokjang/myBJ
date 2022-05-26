arr = [0 for _ in range(26)]
s = input()
s = list(s)
for c in s:
    arr[ord(c.upper()) - 65] = arr[ord(c.upper()) - 65] + 1
max = max(arr)
index = arr.index(max)
cnt = 0
for i in arr:
    if i == max:
        cnt = cnt + 1
    if cnt > 1:
        print('?')
        exit()
print(chr(index + 65))

# if len(list(filter(lambda i: arr[i] == max, range(len(arr))))) >= 2:
#    print('?')
# else:
#    print(chr(index + 65))
