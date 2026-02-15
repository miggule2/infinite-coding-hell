a,b = input().split()
a = int(a)
b = int(b)

array = list(map(int,input().split()))
array.sort()
print(array[b-1])