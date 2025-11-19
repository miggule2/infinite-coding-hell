n = int(input())
video = []
for _ in range(n):
    video.append([int(x) for x in list(input())]) #입력되는 이미지를 이중리스트로 저장

result = []

def quad_tree(r, c, s): #row, column, size
    for i in range(r, r + s):
        for j in range(c, c + s):
            if video[i][j] != video[r][c]: #주어진 크기 내에서 탐색
                result.append("(")
                s_half = s // 2 
                quad_tree(r, c, s_half)  #좌측 위         
                quad_tree(r, c + s_half, s_half)  #우측 위
                quad_tree(r + s_half, c, s_half)  #좌측 아래
                quad_tree(r + s_half, c + s_half, s_half)  #우측아래
                result.append(")")
                return
    result.append(video[r][c])

quad_tree(0, 0, n)
print("".join(map(str, result)))