def zero_one_knapsack(cargo): # cargo는 (가치, 무게)튜플의 리스트
    # 이 코드에서의 전제는 배낭에 담을 수 있는 용량 = 15, 짐개수 = 5
    capacity = 15 # 배낭에 담을 수 있는 용량을 15이기때문
    pack = [] # pack 리스트 변수에 6x16형태의 중간결과 테이블이 생성될 것
              # 6x16인 이유: 짐개수+1(0~5), 배낭용량+1(0~15)으로 테이블을 생성하기 때문

    for i in range(len(cargo)):
        pack.append([])
        for c in range(capacity + 1):
            if i == 0 or c == 0: # 짐이없거나 배낭용량이 0일때는 가치가 0
                pack[i].append(0)

            elif cargo[i-1][1] <= c: # 현재 짐의 무게가 현재 용량보다 작거나 같으면
                pack[i].append(
                    max(
                        cargo[i-1][0] + pack[i-1][c-cargo[i-1][1]],pack[i-1][c] # 짐을 넣는 경우와 안넣는 경우 중 큰값 선택
                    )
                )
            else:
                pack[i].append(pack[i-1][c]) # 현재 짐의 무게가 현재 용량보다 크면 짐을 넣을 수 없으므로 이전값 유지
        return pack[-1][-1] # 최종적으로 배낭에 담을 수 있는 최대 가치를 반환
                            # 테이블에 값을 추가할때 max값을 계속해서 저장했기 때문에 테이블의 가장 마지막값([-1][-1])이 최댓값임