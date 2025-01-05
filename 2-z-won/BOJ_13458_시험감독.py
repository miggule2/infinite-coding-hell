room = int(input())
each_part = list(map(int, input().split()))
main, sub = map(int, input().split())
count = room
for i in each_part:
    remain = i - main
    while remain > 0:
        remain -= sub
        count += 1
print(count)