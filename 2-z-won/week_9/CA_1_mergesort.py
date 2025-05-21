def getInput():
    # stdin으로 입력을 받는 함수
    import sys
    input = sys.stdin.readline
    n = int(input()) # 리스트의 길이
    objective_list = list(map(int, input().split())) # 리스트의 elements

    return n, objective_list

def divide(n, objective_list):
    # 리스트의 길이가 1이 될 때까지 두 부분으로 나누는 함수
    if n == 1:
        return [objective_list]

    # 함수를 절반으로 나눔
    mid = n // 2
    left_half = objective_list[:mid]
    right_half = objective_list[mid:]

    # 나눠진 list를 다시 recursive하게 나눔
    return divide(len(left_half), left_half) + divide(len(right_half), right_half)

def merge(divided_list):
    # 나눠져있는 list를 다시 하나의 sort된 함수로 합치는 함수
    while len(divided_list) > 1:
        merged_list = []

        # 리스트의 앞 부분부터 2개씩 정렬된 함수를 추가하는 부분
        for i in range(0, len(divided_list)-1, 2):
            merged_list.append(mergeLists(divided_list[i], divided_list[i + 1]))
        
        # 리스트의 길이가 홀수일 경우 마지막 element를 추가
        if len(divided_list) % 2 == 1:
            merged_list.append(divided_list[-1])

        divided_list = merged_list
    # 이중리스트로 결과가 저장되어있으므로 빼내줌
    return divided_list[0]


def mergeLists(list1, list2):
    sorted_list = []
    i = j = 0

    #리스트의 elements를 비교하며 sorting하는 부분
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:  
            sorted_list.append(list1[i])
            i += 1
        else:
            sorted_list.append(list2[j])
            j += 1
    
    # 한 쪽에 추가할 남은 element가 없다면 반대쪽 리스트를 추가
    sorted_list += list1[i:]
    sorted_list += list2[j:]
    
    return sorted_list

def displayOutput(sorted_list):
    # 출력 형식에 맞게 출력하는 함수
    for unit in sorted_list:
        print(unit, end=" ")
    print()

def main():
    n, objective_list = getInput()
    divided_list = divide(n, objective_list)
    sorted_list = merge(divided_list)
    displayOutput(sorted_list)

if __name__ == "__main__":
    main()
