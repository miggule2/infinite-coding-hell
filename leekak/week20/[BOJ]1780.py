import sys
sys.setrecursionlimit(3000)

cnt_n = 0    # -1로 채워진 종이 개수
cnt_zero = 0 # 0으로 채워진 종이 개수
cnt_p = 0    # 1로 채워진 종이 개수
paper = []   # 종이 배열

def cut_paper(x, y, N):
    global cnt_n, cnt_zero, cnt_p

    standard_value = paper[y][x]
    is_uniform = True  # 영역이 균일한지 (하나의 값으로만 이루어졌는지) 확인

    # N*N 영역을 순회하며 확인
    for r in range(y, y + N):
        for c in range(x, x + N):
            if paper[r][c] != standard_value:
                is_uniform = False
                break
        if not is_uniform:
            break

    # 영역이 균일하지 않으면 (is_uniform == False) 9개의 작은 영역으로 분할하여 재귀 호출
    if not is_uniform:
        next_N = N // 3
        
        # 3x3 분할하여 재귀 호출
        
        cut_paper(x, y, next_N)
        cut_paper(x + next_N, y, next_N)
        cut_paper(x + 2 * next_N, y, next_N)
        
        cut_paper(x, y + next_N, next_N)
        cut_paper(x + next_N, y + next_N, next_N)
        cut_paper(x + 2 * next_N, y + next_N, next_N)
        
        cut_paper(x, y + 2 * next_N, next_N)
        cut_paper(x + next_N, y + 2 * next_N, next_N)
        cut_paper(x + 2 * next_N, y + 2 * next_N, next_N)

    # 영역이 균일하면 (is_uniform == True) 개수를 카운트
    else:
        if standard_value == -1:
            cnt_n += 1
        elif standard_value == 0:
            cnt_zero += 1
        elif standard_value == 1:
            cnt_p += 1

if __name__ == "__main__":
    try:
        N = int(sys.stdin.readline())
    except:
        N = 0
      
    for _ in range(N):
        # sys.stdin.readline()을 사용하면 한 줄 전체를 읽으므로, split()과 map(int, ...)를 사용해 리스트로 만듭니다.
        # strip()으로 개행 문자를 제거합니다.
        line = list(map(int, sys.stdin.readline().strip().split()))
        paper.append(line)

    cut_paper(0, 0, N)

    print(f"{cnt_n}\n{cnt_zero}\n{cnt_p}")
