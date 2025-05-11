def lotto(arr, count, start, path):
    if count == 6:  # 6개의 숫자를 선택하면 출력
        print(' '.join(map(str, path)))
        return  

    for i in range(start, len(arr)):  # 현재 위치 이후의 숫자만 선택, for문을 이용하여 처음부터 하나씩 키워나가므로 자연스럽게 사전순 정렬됨
        lotto(arr, count + 1, i + 1, path + [arr[i]])  # 재귀 호출

while True:
    ks = list(map(int, input().split()))
    lotto(ks, 0, 1, [])
    print("")
    if ks[0] == 0:
        break
