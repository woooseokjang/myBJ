def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True


n = int(input())
prime = 0
arr = list(map(int, input().split()))
for i in range(n):
    if isPrime(arr[i]):
        prime = prime + 1

print(prime)
