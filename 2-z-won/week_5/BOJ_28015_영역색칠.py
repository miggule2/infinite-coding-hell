def solve():
    import sys
    input = sys.stdin.readline
    
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    
    total_brush = 0
    
    for r in range(N):
        row = board[r]
        
        c = 0
        while c < M:
            if row[c] == 0:
                c += 1
                continue
            
            s = c
            while c < M and row[c] != 0:
                c += 1
            e = c
            segment = row[s:e]
            blocks1 = 0
            blocks2 = 0
            prev_color = 0
            
            for color in segment:
                if color != prev_color:
                    if color == 1:
                        blocks1 += 1
                    else:  # color == 2
                        blocks2 += 1
                prev_color = color
        
            brush_for_segment = 1 + min(blocks1, blocks2)
            
            total_brush += brush_for_segment
    
    print(total_brush)
