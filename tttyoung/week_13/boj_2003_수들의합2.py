#다른방법으로도 풀어보기
n, m = map(int, input().split())
numlist = list(map(int, input().split()))

def numhap(numlist, m):
    start = end = count = 0
    sum = numlist[start]
    while start <len(numlist) and end < len(numlist):
        if sum < m:
            end += 1
            if end == len(numlist):
                break
            sum += numlist[end]
        elif sum > m:
            sum -= numlist[start]
            start += 1
        else:
            count += 1
            sum -= numlist[start]
            start += 1
    return count

print(numhap(numlist, m))
