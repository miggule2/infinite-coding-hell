def merge_sort(a):
    if len(a) == 1:
        return a
    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    return merge_g(left, right)

def merge_g(g1, g2):
    i = j = 0
    result =[]
    while i<len(g1) and j<len(g2):
        if g1[i]<g2[j]:
            result.append(g1[i])
            i+=1
        else:
            result.append(g2[j])
            j+=1
    
    if i == len(g1):
        result+=g2[j:]
    if j == len(g2):
        result+=g1[i:]
    return result

num = int(input())
arr = []
for i in range(num):
    n = int(input())
    arr.append(n)

for i in merge_sort(arr):
    print(i)