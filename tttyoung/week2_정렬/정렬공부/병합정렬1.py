#새로운 리스트 만들지 않고 기존 리스트내에서 정렬하여 한 함수로 구현 - 최적화

def merge_sort(a):
    n = len(a)
    #종료조건: 정렬할 리스트의 자료개수가 1이하라면 정렬필요X
    if n<=1:
        return
    mid = n//2 #그룹나누기
    g1 = a[:mid] #처음부터 mid전까지를 변수 g1에 입력
    g2 = a[mid:] #mid부터 끝까지를 변수 g2에 입력
    merge_sort(g1) #재귀
    merge_sort(g2)

    #두그룹 병합하기
    i1 = 0
    i2 = 0
    ia = 0

    while i1<len(g1) and i2<len(g2): #g1/g2에 자료가 하나라도 남을때까지 while문을 반복
        if g1[i1] <g2[i2]:
            a[ia] = g1[i1]
            i1+=1
            ia+=1
        else:
            a[ia] = g2[i2]
            i2+=1
            ia+=1
            
    #한쪽 자료개수 0, 나머지 한쪽에는 자료가 남아있는 경우 합쳐줌
    while i1<len(g1):
        a[ia] = g1[i1]
        i1+=1
        ia+=1

    while i2<len(g2):
        a[ia] = g2[i2]
        i2+=1
        ia+=1

d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
merge_sort(d)
print(d)