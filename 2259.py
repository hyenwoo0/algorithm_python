A, B = map(int, input().split())
arr = list(map(int, input().split()))

prefix = [0 for _ in range(A+1)] # 1칸더 크게 만들

for i in range(A):
    prefix[i+1] = prefix[i] + arr[i]

print(arr)
print(prefix)