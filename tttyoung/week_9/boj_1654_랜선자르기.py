k, n = map(int, input().split())
lanlist = [int(input()) for _ in range(k)]

def binary(lanlist, n, start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        if mid == 0: #만약 입력이 4, 4 / 1, 1, 1, 1일 경우에는 mid가 0이 됨. 따라서 예외처리를 하여 while문 탈출
            result = 1
            break
        count = 0
        for i in lanlist: #지금의 mid로 자를 수 있는 최대의 랜선갯수 구하기
            if i >= mid: 
                count += (i // mid) #mid가 0인 경우에는 zerodivisionerror가 발생함. 0으로 나눠질 수 없기 때문에 위에서 mid가 0일때 예외처리를 해야함.

        if count >= n: #만약 우리가 구하는 랜선보다 많거나 같은 개수만큼을 얻게된다면 현재의 미드보다 더 큰 값으로 n에 더 근접한 개수를 구할 수도 있음. 
            start = mid + 1 #start를 mid 다음수로 설정 후 다시 while문 반복
            result = mid #일단 결과값(최대 길이)에 현재의 mid를 저장 후 while문을 더 돌면서 이보다 큰값이 만족하는지를 확인함.
        else:
            end = mid - 1 
    return result

print(binary(lanlist, n, 0, max(lanlist)))

