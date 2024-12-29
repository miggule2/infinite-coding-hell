def ins_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j]<arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]

def adding(arr1):
    count = 0
    for i in range(0, len(arr1)-1):
        for j in range(i+1, len(arr1)):
            if arr1[i] + arr1[j] == add:
                count+=1
    print(count)

num = int(input())
num_list = list(map(int, input().split()[:num]))
add = int(input())

ins_sort(num_list)
adding(num_list)
