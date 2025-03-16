num = int(input())
plist = []
for i in range(num):
    plist.append(list(map(str, input().split())))
    plist[i][0] = int(plist[i][0]) #입력은 str형태로 받았기 때문에 숫자는 int형으로 변환해줌.그러지 않으면 정렬과정에서 문제가 발생함.

plist.sort(key = lambda x:x[0]) #다중리스트나 딕셔너리같이 리스트내에 하나의 객체만 있는것이 아닐때, lambda를 이용하여 원하는 키값에 대한 정렬을 할 수 있음

for j in range(num):
    print(' '.join(map(str, plist[j])))