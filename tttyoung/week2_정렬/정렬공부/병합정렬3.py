# 새로운 함수 result를 만들어 merge_sort()-재귀 및 정렬하는 함수, merge_g()-병합하는 함수 총 2개의 함수를 만들어 구현
def merge_sort(a):
    n = len(a)
    #종료조건: 정렬할 리스트의 자료개수가 1이하라면 정렬필요X
    if n<=1:
        return a
    mid = n//2 #그룹나누기
    left = merge_sort(a[:mid]) #재귀
    right = merge_sort(a[mid:])
    
    return merge_g(left, right)

#두그룹 병합하기
def merge_g(g1, g2):
    i1 = i2 = 0
    result =[]

    while i1<len(g1) and i2<len(g2): #g1/g2에 자료가 하나라도 남을때까지 while문을 반복
        if g1[i1] <g2[i2]:
            result.append(g1[i1])
            i1+=1
        else:
            result.append(g2[i2])
            i2+=1
            
    #아직 남아있는 자료들을 결과에 추가
    if i1 == len(g1):
        result += g2[i2:]
    if i2 == len(g2):
        result += g1[i1:]
    return result

d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
print(merge_sort(d))