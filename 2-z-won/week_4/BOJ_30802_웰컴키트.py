import math

n = int(input())
shirts_list = list(map(int, input().split()))
T, P = map(int, input().split())

count = 0
for i in shirts_list:
    count += math.ceil(i/T)

print(count)
print(n//P, n%P)
