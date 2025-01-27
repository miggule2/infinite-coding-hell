n, m = map(int, input().split())

pok_dicnum = {} #번호 저장할 딕셔너리
pok_dicstr = {} #이름 저장할 딕셔너리
#이름 번호 같이 저장하면 찾는데 for문을 이중으로 사용해야해서 오래걸림
for i in range(n):
    a = input()
    pok_dicnum[i+1] = a
    pok_dicstr[a] = i + 1

result = []
for i in range(m):
    a = input()
    if a.isdigit():
        result.append(pok_dicnum[int(a)])
    elif a.isalpha():
        result.append(pok_dicstr[a]) 

for i in result:
    print(i)

