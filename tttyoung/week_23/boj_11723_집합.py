import sys
input = sys.stdin.readline #input()을 사용하면 시간초과과

m = int(input())
s = set() #연산 개수가 최대 300만개가 되기 때문에 리스트로 하면 최대 O(n)의 시간복잡도를 가짐. 따라서 집합인 set을 사용

for _ in range(m): #m번의 연산산
    c = list(input().split())
    #c[1]은 str로 입력을 받기 때문에 사용시에는 int로 변환하여 사용해야함.
    if c[0] == 'add':
        s.add(int(c[1])) #set에는 append대신 add사용
    elif c[0] == 'remove' and int(c[1]) in s:
        s.remove(int(c[1]))
    elif c[0] == 'check':
        if int(c[1]) in s:
            print(1)
        else:
            print(0)
    elif c[0] == 'toggle':
        if int(c[1]) in s:
            s.remove(int(c[1]))
        else:
            s.add(int(c[1]))
    elif c[0] == 'all':
        s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
    elif c[0] == 'empty':
        s = set() #빈 집합 사용시에는 set() 사용
