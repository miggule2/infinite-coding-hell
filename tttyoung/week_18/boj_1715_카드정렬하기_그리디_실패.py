from collections import deque
#입력받은 카드 수 리스트를 정렬하여 앞에 2개를 묶어서 합침. 이때 합한 수는 result에 누적
#앞의 2개의 카드묶음을 더한 후 index 1에 대입하고 index 0을 popleft하여 지움.
#실패 사유: 시간초과 / 한번 합칠때마다 덱을 정렬해야하므로 N이 100,000일때 시간복잡도가 적어도 100,000log(100,000)

def sort_card(cardnum):
    result = 0
    cardnum = deque(sorted(cardnum)) #초기 덱 정렬렬
    while len(cardnum)>1: #카드 묶음이 1개가 남을때까지
        if cardnum[0] > cardnum[1]: #시간초과 해결하려고 모든 경우에 정렬이 아닌 index 0 이 index 1보다 큰 경우에만 정렬을 시도도
            cardnum = deque(sorted(cardnum))
        #카드 묶음 합친후, result 갱신, popleft하여 합쳐진 카드리스트를 만듦
        cardnum[1] = cardnum[0] + cardnum[1] 
        result += cardnum[1]
        cardnum.popleft()
    return result

N = int(input())
card_num = deque([int(input()) for _ in range(N)])
print(sort_card(card_num))
