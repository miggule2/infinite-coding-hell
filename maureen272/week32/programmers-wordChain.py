def solution(n, words):
    # 이미 나온 단어를 저장할 집합
    seen = set()
    seen.add(words[0])
    
    for i in range(1, len(words)):
        word = words[i] # 현재 단어
        prev_word = words[i-1] # 이전 단어
        
        # 탈락 조건 1: 이전 단어의 끝 글자로 시작하지 않음
        # 탈락 조건 2: 이미 등장했던 단어임
        if word[0] != prev_word[-1] or word in seen:
            # 탈락자 번호와 차례 계산
            player_num = (i % n) + 1
            turn_num = (i // n) + 1
            return [player_num, turn_num]
        
        # 통과했다면 단어장에 추가
        seen.add(word)

    # 끝까지 탈락자가 없으면 [0, 0] 반환
    return [0, 0]