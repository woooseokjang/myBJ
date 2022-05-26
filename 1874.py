n = int(input())
s = []
o = []
cur = 1
flag = False
for i in range(n):
    num = int(input())
    if flag:
        None
    else:
        while cur <= num:
            s.append(cur)
            o.append('+')
            cur = cur + 1
        o.append('-')
        if s.pop(-1) != num:
            flag = True
if flag:
    print("NO")
else:
    for c in o:
        print(c)
