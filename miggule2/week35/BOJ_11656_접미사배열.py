string = input()
array = []
for i in range(len(string)) :
    array.append(string[i:])
array.sort()

for i in array :
    print(i)

# method2 : 인덱스만 활용해서 정렬하기
string = input()
# 각 접미사 시작 인덱스만 저장
indecies = list(range(len(string)))
# 인덱스를 정렬하되, 비교 기준을 접미사들로 해서 정렬
indecies.sort(key = lambda i : string[i:])

for i in indecies :
    print(string[i:])
