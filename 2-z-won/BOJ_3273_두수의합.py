"""
n개의 서로 다른 양의 정수... 라는 표현 덕분에
set을 사용하여 해결
알고리즘 분류의 투포인터를 사용하지 않아도 괜찮을
표본 크기와 시간임
"""
n = int(input())
input_list = list(map(int, input().split()))
input_set = set(input_list)
x = int(input())

count = 0

for i in input_list:
    target = x - i
    if target in input_set:
        count += 1

# 중복제거
print(count//2)