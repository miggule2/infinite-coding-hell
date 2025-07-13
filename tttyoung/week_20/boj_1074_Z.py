count = 0 
def Z(n, x, y):
    global count
    if n == 0:
        return 
    
    h = 2**(n-1)
    #각 사분면마다 시작숫자를 count로 다르게 해주고, 재귀할때 x, y 즉 좌표값을 쪼개서 수정하여 최종목적 좌표가 도달하게함
    if x<h and y<h: #1사분면
        count += 0 
        return Z(n-1, x, y)
    elif x<h and y>=h: #2사분면
        count += h*h 
        return Z(n-1, x, y-h)
    elif x>=h and y<h: #3사분면
        count += h*h*2
        return Z(n-1, x-h, y)
    elif x>=h and y>=h: #4사분면
        count += h*h*3
        return Z(n-1, x-h, y-h) 

N, r, c = map(int, input().split())
Z(N, r, c)
print(count)