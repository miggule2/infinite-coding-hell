def fractional_knapsack(cargo):
    capacity = 15
    pack = []
    # 단가 계산 역순 정렬
    for c in cargo:
        pack.append((c[0] / c[1], c[0], c[1])) # (단가, 가치, 무게)
    pack.sort(reverse=True) # 단가 역순 정렬

    total_value = 0
    for p in pack:
        if capacity >= p[2]: # 현재 배낭 용량이 물건 무게보다 크면
            capacity -= p[2] # 배낭 용량에서 물건 무게만큼 빼기
            total_value += p[1] # 물건 가치 더하기
        else: # 현재 배낭 용량이 물건 무게보다 작으면
            total_value += p[0] * capacity # 남은 용량만큼 단가 * 남은 용량 더하기
            break # 배낭이 꽉 찼으므로 종료
    return total_value