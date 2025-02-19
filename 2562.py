import sys

num = []
for i in range(9):
    num.append(int(sys.stdin.readline().strip()))
max_value = max(num)
index = num.index(max_value)
print(max_value)
print(index+1)

