n = int(input())
input_list = list(map(int, input().split()))
input_set = set(input_list)
x = int(input())

count = 0

for i in input_list:
    target = x - i
    if target in input_set:
        count += 1

# 중복제거
print(count//2)