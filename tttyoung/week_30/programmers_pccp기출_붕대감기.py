def solution(bandage, health, attacks): 
    #bandage = 기술시전시간, 1초당회복량, 추가회복량
    #attacks = 공격시간, 공격량

    cur_health = health
    for i in range(len(attacks)-1): #마지막 공격 직전까지의 공격과 회복
        cur_health -= attacks[i][1] #공격시 체력감소
        if cur_health <= 0: return -1 
        sub_time = attacks[i+1][0] - attacks[i][0] - 1 #다음공격까지의 시간 (피회복시간)
        cur_health += sub_time * bandage[1] + (sub_time//bandage[0]) * bandage[2] #추가회복량 포함
        if cur_health > health: cur_health = health
    
    cur_health -= attacks[-1][1] #마지막 공격으로 인한 체력감소
    if cur_health <= 0: return -1
    answer = cur_health
    return answer
