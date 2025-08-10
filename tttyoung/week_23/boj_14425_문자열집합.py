import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = set() #집합사용용
count = 0 #개수수

for _ in range(n): #주어진 s집합 입력
    s.add(input()) 
for _ in range(m): #m개의 문자열을 돌면서 이 중에 입력된 s집합과 공통된것이 있는지 확인
    x = input()
    if x in s:
        count+=1 #공통된 값일때 count+1

print(count)
