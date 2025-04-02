def plus_cycle(num):
    firstnum = num
    count = 0
    new_num = -1
    while True:
        new_num = num//10 + num%10
        new_num = new_num%10 + 10*(num%10)
        count += 1
        if new_num == firstnum: break
        num = new_num
    return count

print(plus_cycle(int(input())))