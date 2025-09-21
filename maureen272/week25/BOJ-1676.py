# BOJ : 1676 - 팩토리얼 0의 개수
N = int(input())
count = 0

# N!에 들어있는 5의 개수를 누적해서 셈
i = 5
while N // i > 0:
    count += N // i
    i *= 5

print(count)
