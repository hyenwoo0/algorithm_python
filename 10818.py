import sys

n = int(sys.stdin.readline().strip())  
num = []

num = list(map(int, sys.stdin.readline().strip().split()))

print(min(num), max(num))
