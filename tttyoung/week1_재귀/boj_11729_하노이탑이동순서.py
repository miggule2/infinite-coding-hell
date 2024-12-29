#hanoi(n-1) -> mid_h   ||   가장 큰 원판-> to_h   ||   mid_h에 있는 hanio(n-1) -> to_h


def hanoi(n, from_h, to_h, mid_h): #하노이탑 이동순서 함수
    #n은 원판 갯수, from_h는 출발막대, to_h는 도착막대, mid_h는 중간막대(거쳐가는)

    if n==1: #재귀함수 종료조건 
        return print(from_h, to_h)
    
    hanoi(n-1, from_h, mid_h, to_h) #가장 큰 원판 제외(n-1개의 원판)을 from -> mid로 옮김
    print(from_h, to_h) #가장 큰 원판을 from -> to로 옮김
    hanoi(n-1, mid_h, to_h, from_h) #mid에 있는 n-1개의 원판 -> to로 옮김

def hanoi_count(n): #하노이탑 총 이동횟수구하는 함수 || #참고) 하노이탑 횟수 공식: count = 2**n-1
    if n == 1:
        return 1
    return hanoi_count(n-1) * 2 + 1    

num = int(input())

print(hanoi_count(num))
hanoi(num, 1, 3, 2)

