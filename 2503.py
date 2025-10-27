import sys
input = sys.stdin.readline

N = int(input())
questions = [tuple(input().split()) for _ in range(N)]

answer = 0

for i in range(1, 10):
    for j in range(1, 10):
        if i == j:
            continue
        for k in range(1, 10):
            if i == k or j == k:
                continue

            candidate = str(i) + str(j) + str(k)
            is_valid = True

            for q_num, s, b in questions:
                strike = 0
                ball = 0

                for a in range(3):
                    if candidate[a] == q_num[a]:
                        strike += 1
                    elif candidate[a] in q_num:
                        ball += 1

                if strike != int(s) or ball != int(b):
                    is_valid = False
                    break

            if is_valid:
                answer += 1

print(answer)
