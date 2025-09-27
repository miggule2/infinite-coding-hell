s = input()
result = []
for i in range(len(s)): #문자열을 돌면서 이어지는 문자열 정리
    for j in range(1, len(s)+1):
        result.append(s[i:j]) 

result = list(set(result)) #문자열 내에 중복되는 값들 제거
print(len(result) - 1) # 문자열 특성상 null값이 있기 때문에 null을 제외한 개수 출력