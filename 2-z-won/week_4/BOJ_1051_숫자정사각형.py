
a, b = map(int, input().split())
num_list = []

for _ in range(a):
    app_list = list(map(str, input().split()))
    num_list.append(app_list)

for row in num_list:
    temp = row[0]
    for digit in row:
        continue
