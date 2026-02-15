s = input()
l = []
for i in range(len(s)):
    l.append(s[i:len(s)]) #앞에서부터 하나씩 줄여가며 슬라이싱
l.sort() #사전순 정렬
for i in l:
    print(i) 