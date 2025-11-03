import sys
from collections import deque

def solve():
    try:
        # sys.stdin.readline()은 개행 문자를 포함하므로 strip()으로 제거
        N = int(sys.stdin.readline().strip())
    except:
        print(1) 
        return
      
    Q = deque(range(1, N + 1))

    while len(Q) > 1:
        Q.popleft() 
        card_to_move = Q.popleft()
        Q.append(card_to_move)

    if Q:
        print(Q[0]) # 또는 print(Q.popleft())

if __name__ == "__main__":
    solve()
