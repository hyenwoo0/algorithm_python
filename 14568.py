import sys

candy = int(sys.stdin.readline()) # 6

num = 0

for A in range(1, candy+1): # 택희
    for B in range(1, candy+1): # 영훈
        for C in range(1, candy+1): # 남규
            if A + B + C == candy:
                if C >= B+2:
                    if A != 0 and B != 0 and C != 0:
                        if A % 2 ==0:
                            num += 1
print(num)
