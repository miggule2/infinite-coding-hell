num = int(input())
P = list(map(int, input().split()))

def sel_sort(p): #리스트p를 선택정렬을 이용하여 오름차순으로 정렬
    for i in range(0, len(p)-1):
        min_idx = i
        for j in range(i+1, len(p)):
            if p[j]<p[min_idx]:
                min_idx = j
        p[min_idx], p[i] = p[i], p[min_idx]

def hap(l): #리스트 l의 합 구하는 함수
    f = 0
    for i in range(0, len(l)):
        for j in range(0, i+1):
            f+=l[j]
    return f

sel_sort(P)
print(hap(P))