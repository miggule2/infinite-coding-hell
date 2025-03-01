def armor(alist, m):
    low = count = 0
    high = len(alist) - 1

    while low < high:
        if alist[low] + alist[high] < m:
            low += 1
        elif alist[low] + alist[high] > m:
            high -= 1
        elif alist[low] + alist[high] == m:
            count += 1
            low += 1
    return count

n = int(input())
m = int(input())
armorlist = list(map(int, input().split()))
armorlist.sort()

print(armor(armorlist, m))