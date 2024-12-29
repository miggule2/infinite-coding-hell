# 새로운 리스트 result를 만들어 정렬하여 한 함수로 구현
def merge_sort(a):
    n = len(a)
    #종료조건: 정렬할 리스트의 자료개수가 1이하라면 정렬필요X
    if n<=1:
        return a
    mid = n//2 #그룹나누기
    g1 = merge_sort(a[:mid]) #처음부터 mid전까지를 재귀한 값을 변수에 입력
    g2 = merge_sort(a[mid:]) #mid부터 끝까지를 재귀

    i1 = i2 = 0
    result =[]

    while i1<len(g1) and i2<len(g2): #g1/g2에 자료가 하나라도 남을때까지 while문을 반복
        if g1[i1] <g2[i2]:
            result.append(g1[i1])
            i1+=1
        else:
            result.append(g2[i2])
            i2+=1
            
    #한쪽 자료개수 0, 나머지 한쪽에는 자료가 남아있는 경우 합쳐줌
    if i1 == len(g1):
        result += g2[i2:]
    if i2 == len(g2):
        result += g1[i1:]
    return result

d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
print(merge_sort(d))
#https://www.daleseo.com/sort-merge/