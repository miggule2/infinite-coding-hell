def ins_sort(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i-1
        while j>=0 and a[j]>key:
            a[j+1] = a[j]
            j-=1
        a[j+1] = key
        print(i, a)

d = [2, 4, 3, 1, 6, 8, 0]
ins_sort(d)
print(d)