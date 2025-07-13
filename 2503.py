import sys

N = int(sys.stdin.readline())

data = []
for _ in range(N):
    M = list(map(int, sys.stdin.readline().split()))
    data.append(M)

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):

