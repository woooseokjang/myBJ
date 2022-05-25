n = int(input())
hit = 0
i = 0
while True:
    temp = str(i)
    if -1 != temp.find("666"):
        hit = hit + 1
    if hit == n:
        print(i)
        exit()
    i = i + 1
