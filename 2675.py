import sys

a = int(sys.stdin.readline().strip())
for i in range(a):
    b, c = sys.stdin.readline().split()
    b = int(b)
    for char in c:
        print(char * b, end="")
    print()
