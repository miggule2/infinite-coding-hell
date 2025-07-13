white = 0
blue = 0

#return값을 사용하게 되면 1 1이 입력될때 바로 if문 조건을 만족하여 그냥 return이 되므로 전역변수값을 출력하도록한다.
def cut_paper(N, paper):
    global white, blue
    if N < 1: #1보다 작으면 자르기 불가능
        return 
    if all(cell == 1 for row in paper for cell in row): #선택구간이 1로 차있을때
        blue += 1
        return
    if all(cell == 0 for row in paper for cell in row): #선택구간이 0으로 차있을때
        white += 1
        return
    else: #위 사항에 해당되지 않는 경우(해당구간을 다시 나눠야하는경우)
        N = N//2 
        cut_paper(N, [row[0:N] for row in paper[0:N]])
        cut_paper(N, [row[N:2*N] for row in paper[0:N]])
        cut_paper(N, [row[0:N] for row in paper[N:2*N]])
        cut_paper(N, [row[N:2*N] for row in paper[N:2*N]])
    
N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
cut_paper(N, paper)
print(white)
print(blue)