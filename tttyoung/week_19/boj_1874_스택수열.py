n = int(input())

new_st = []
result = []
p = 0 #오름차순으로 하나씩 push가능하기 때문에 해당값을 저장할 변수

for _ in range(n):
    num = int(input())
    while p < num: #수열준비과정, push를 해서 p값 조정 및 pop을 통해 만들 수열의 기반수열을 만듦.+
        p+=1
        new_st.append(p)
        result.append("+")
    if new_st[-1] == num: #pop하는 과정, pop을 통해 우리가 원하는 해당 수열을 result에 저장함. 
        new_st.pop()
        result.append("-")
    else: #불가능한 수열, 만약 pop해야되는 값이 new_st의 마지막값이 아닌 중간값이라면 pop을 통해 수열만들기 불가능.
        result.clear()
        result.append("NO")
        break

print('\n'.join(result))
