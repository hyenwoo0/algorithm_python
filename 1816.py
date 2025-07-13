import sys

N = int(input())

for _ in range(N):
    num = int(input())
    for i in range(2, 1000001):
        if num % i == 0:
            print("NO")
            break
        if i == 1_000_000:
            print("YES")
