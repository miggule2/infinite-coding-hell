num, want = map(int, input().split())

every_info = []
for _ in range(num):
    info = list(map(int, input().split()))
    every_info.append(info)
every_info = sorted(every_info, key = lambda x: (-x[1],-x[2],-x[3]))
print(every_info)
grade, dongsu = 1, 0

for i in range(num-1):
    if every_info[i][1:] == every_info[i+1][1:]:
        dongsu += 1
    else:
        if dongsu:
            grade += dongsu
            dongsu = 0
        grade += 1
    if every_info[i][0] == want:
        print(grade)
        break