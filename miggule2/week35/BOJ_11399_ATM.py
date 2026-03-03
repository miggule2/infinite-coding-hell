n = int(input())

array = list(map(int,input().split()))
array.sort()

s = 0
result = 0
for num in array :
    s += num
    result += s
print(result)