s = input()
flag = False #괄호 내에 있는 단어 여부
result = ''
temp = '' #임시저장용 배열

for i in s:
    if i == "<": 
        if temp: #<를 만나고 임시배열에 있을경우
            result+=temp[::-1]
            temp = ''
        flag = True
        result+=i
    elif i == ">":
        flag = False #flag 닫기
        result+=i
    elif flag:
        result+=i
    else:
        if i.isspace(): #공백만나면 임시배열 뒤집어서 출력 후 공백까지 추가
            if temp:
                result+=temp[::-1]
                result+=i
                temp = ''
        else: temp+=i
if temp: #마지막 문자들이 임시배열에 있는 경우
    result+=temp[::-1]
    temp = '' 

print(result)
