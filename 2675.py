import sys


def myprint(i, c):
    for _ in range(int(i)):
        print(c, end='')


t = int(sys.stdin.readline())

for i in range(t):
    r = list(sys.stdin.readline())
    for j in r[2:-1]:
        myprint(r[0], j)
    print()
