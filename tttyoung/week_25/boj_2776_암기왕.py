def binary_search(n_list, i):
    start, end = 0, len(n_list)-1 # -1 안해주면 index error
    while start <= end:
        mid = (start + end) // 2
        if n_list[mid] == i: #mid의 index에 해당하는 값이 i와 같으면 1 return하면서 함수 종료
            return 1
        elif n_list[mid] < i:
            start = mid + 1
        else: 
            end = mid - 1
    return 0 #while문을 끝까지 반복해도 if문에 해당하지 않는다면 없다는것이니 0 return

t = int(input())
for _ in range(t):
    n = int(input())
    n_list = list(map(int, input().split()))
    n_list.sort() #이분탐색을 하기 위해 정렬
    m = int(input())
    m_list = list(map(int, input().split()))
    for i in m_list:
        print(binary_search(n_list, i))