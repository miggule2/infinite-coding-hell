def is_hansu(numString):
    # 한자리 수와 두자리 수는 모두 한수이다.
    if len(numString) <= 2:
        return True
    # 세자리 수는 십의자리 수가 등차중항이면 한수이다.
    elif len(numString) == 3:
        if int(numString[0]) + int(numString[2]) == 2 * int(numString[1]):
            return True
        else:
            return False
    else:
        return False

def count_hansu(num):
    count = 0
    for i in range(1, num+1):
        if is_hansu(str(i)):
            count += 1
    return count

num = int(input())
print(count_hansu(num))
