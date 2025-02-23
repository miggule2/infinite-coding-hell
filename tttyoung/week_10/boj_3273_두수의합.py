num = int(input())
num_list = list(map(int, input().split()[:num]))
target_add = int(input())

num_list.sort()

def two_pointer(numlist, targetadd):
    low = count = 0
    high = len(numlist) - 1 #투포인터를 양쪽 끝으로 잡음
    while low < high:
        if numlist[low] + numlist[high] < targetadd:
            low += 1 #타겟값보다 작다면 low+1을 하여 값이 커지도록함.

        elif numlist[low] + numlist[high] > targetadd:
            high -= 1 #타겟값보다 크다면 high-1을 하여 값이 작아지도록함.

        elif numlist[low] + numlist[high] == targetadd:
            count += 1
            low += 1 #타겟값과 일치하다면 low+1을 하여 다음 값들부터 볼 수 있도록 함.
    return count

print(two_pointer(num_list, target_add))