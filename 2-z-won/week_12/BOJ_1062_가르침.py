import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def main():
    N, K = map(int, input().split())
    words = [input().strip() for _ in range(N)]
    
    # 가르쳐야 하는 글자: a, n, t, i, c
    if K < 5:
        print(0)
        return
    
    base_mask = 0
    for c in 'antic':
        base_mask |= 1 << (ord(c) - ord('a'))
    
    # 각 단어를 비트마스크로 변환
    word_masks = []
    for w in words:
        m = 0
        for ch in set(w):
            m |= 1 << (ord(ch) - ord('a'))
        word_masks.append(m)
    
    # 베이스 마스크에 이미 포함된 글자를 제외한 후보 글자 인덱스 리스트
    candidates = [i for i in range(26) if not (base_mask & (1 << i))]
    L = len(candidates)
    need = K - 5   # 추가로 골라야 할 글자 수
    
    ans = 0
    def dfs(idx, cnt, mask):
        nonlocal ans
        # 필요한 글자 수만큼 골랐을 때
        if cnt == need:
            cnt_readable = 0
            for wm in word_masks:
                # 단어에 포함된 모든 글자가 mask에 포함되어 있으면 읽을 수 있다
                if (wm & mask) == wm:
                    cnt_readable += 1
            ans = max(ans, cnt_readable)
            return
        
        # 후보가 다 떨어졌거나, 남은 후보가 부족하면 중단
        if idx == L or cnt + (L - idx) < need:
            return
        
        # candidates[idx] 글자 선택
        dfs(idx + 1, cnt + 1, mask | (1 << candidates[idx]))
        # 선택하지 않음
        dfs(idx + 1, cnt, mask)
    
    # 탐색 시작 (초기 mask에는 'antic' 5글자만 포함)
    dfs(0, 0, base_mask)
    print(ans)

if __name__ == "__main__":
    main()
