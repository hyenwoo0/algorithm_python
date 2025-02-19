import sys

A = int(sys.stdin.readline().strip())

B = sys.stdin.readline().strip()

sum = 0

for i in B:
    sum += int(i)

print(sum)