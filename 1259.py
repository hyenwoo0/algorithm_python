import sys

def reverse_number(n):
    return int(str(n)[::-1])


while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    if reverse_number(n) == n:
        print("yes")
    else:
        print("no")

