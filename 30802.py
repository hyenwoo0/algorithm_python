import sys
import math

N = int(sys.stdin.readline())
sizes = list(map(int, sys.stdin.readline().split()))
T, P = map(int, sys.stdin.readline().split())

shirt_bundles = 0
for s in sizes:
    shirt_bundles += math.ceil(s / T)

pen_bundles = N // P
pen_individuals = N % P

print(shirt_bundles)
print(pen_bundles, pen_individuals)