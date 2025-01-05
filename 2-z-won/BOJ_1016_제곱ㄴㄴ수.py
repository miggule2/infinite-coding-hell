import math

# 입력 받고~
mini, maxi = map(int, input().split())
domain = maxi - mini + 1
# 마킹하고~
mark = [False] * domain

for i in range(2, int(math.sqrt(maxi))+1):
    square = i*i

    start = (mini // square) * square
    if start < mini:
        start += square
    
    # 막 효율적인지는 모르겠는데 그냥 뭐 대충해도 될거같은데 억지 에라토스테네스의 체 했음
    # 알고리즘 분류에 소수판별 이런거 있던데 안써서 의도대로 푼 것인지는 모르겠음
    for multiple in range(start, maxi+1, square):
        mark[multiple - mini] = True

# count 해도 시간초과 안남 개꿀임
count = mark.count(False)
print(count)