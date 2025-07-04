import sys
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

count = 0
for i in num:
    if is_prime(i):
        count += 1

print(count)
