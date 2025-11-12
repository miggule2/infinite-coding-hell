# lv4
def solution(money):
    n = len(money)
    if n == 3: # 예외 처리(집이 3채면 한 집밖에 털지못함)
        return max(money)

    # dp1, dp2는 각 case에 따른 최대 금액을 저장하는 리스트
    dp1 = [0] * n  # 첫 집을 털었을 때 
    dp2 = [0] * n  # 첫 집을 안 털었을 때

    # 첫 집을 털었을 경우 -> 마지막 집 털 수 x
    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])
    for i in range(2, n - 1): # 마지막 집을 털 수 없기 때문에 n-1까지
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + money[i]) # i번째 집 털지 않았을 경우 vs 털었을 경우(i-2번째 집까지의 최대 금액 + 현재 집 금액)

    # 첫 집을 털지 x -> 두 번째 집부터 시작 & 마지막 집 털 수 o
    dp2[0] = 0
    dp2[1] = money[1]
    for i in range(2, n): # 마지막 집을 털 수 있기 때문에 n까지
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + money[i])

    # 두 경우 중 큰 값 선택
    return max(dp1[n - 2], dp2[n - 1])
