def getInput():
    a, b = map(int, input().split())
    num_list = []
    for _ in range(a):
        num_list.append(list(input()))
    return a, b, num_list

def check_square(a, b, num_list):
    k = min(a,b)
    for k in range(min(a, b)-1, -1, -1):
        for i in range(a-k):
            for j in range(b-k):
                if num_list[i][j] == num_list[i][j+k] == num_list[i+k][j] == num_list[i+k][j+k]:
                    return (k+1)*(k+1) 

def main():
    a, b, num_list = getInput()
    surface = check_square(a,b,num_list)
    print(surface)

main()
