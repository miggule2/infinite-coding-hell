#삽입정렬
#시간초과
def sel_sort(a):
    for i in range(1, len(a)):
        for j in range(i, 0, -1):
            if a[j]<a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]

num = int(input())
arr = []
for i in range(num):
    n = int(input())
    arr.append(n)

sel_sort(arr)
for i in arr:
    print(i)