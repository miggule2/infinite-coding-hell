def solution(people, limit):
    answer = 0
    # 몸무게 오름차순 정렬
    people.sort()
    
    light = 0 # 가장 가벼운 사람을 가리키는 idx
    heavy = len(people) - 1 # 가장 무거운 사람을 가리키는 idx
    
    while light <= heavy:
        # 가장 가벼운 사람 + 가장 무거운 사람의 합이 제한 이하인지 확인
        if people[light] + people[heavy] <= limit: # 두 명 같이 탈 수 있으면 가벼운 사람도 인덱스 이동
            light += 1
        
        heavy -= 1 # 무거운 사람은 무조건 보트에 탐 (혼자든 같이든)
        answer += 1 # 보트 개수 추가 
        
    return answer