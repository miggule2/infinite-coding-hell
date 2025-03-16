#다른방법으로도 풀어보기
def fibonacci(n, memo):
    if n == 0:
        return [0, 1, 0]
    elif n == 1: 
        return [1, 0, 1]
    
    if memo[n][0] is not None:
        return memo[n]
    #memo[n] = fibonacci(n-1, cnt, memo) + fibonacci(n-2, cnt, memo) 원래의 점화식으로 memo에 피보나치 수열값만 저장이 됨 n==0, 1일때 cnt를 더해준다고 해서 memo에서 값을 가져올때 cnt가 저장되는것이 아님.
    fib1, z1, o1 = fibonacci(n-1, memo)
    fib2, z2, o2 = fibonacci(n-2, memo)

    memo[n] = [fib1 + fib2, z1 + z2, o1 + o2]

    return memo[n]
    
    
t = int(input())

for _ in range(t):
    n = int(input())
    memo = [[None, 0, 0] for _ in range(n+1)]  #현재 cnt값들은 memo에 저장되지않아서 memo에서 값을 가져올때도 cnt값을 같이 가져와줘야하는데 그 과정이 생략되어있음.그치만 정확이 왜 22입력일때 1 2가 나오는지 모르겠음.해결완료. 
    result = fibonacci(n, memo)
    print(result[1], result[2])
    #memo[n][1], memo[n][2]을 출력하려고 했으나 n = 0이나 1일 경우에는 fibonacci함수에서 나오는게 [0, 1, 0] [0, 1, 0]임. 이 경우에 그냥 바로 return한 것이지 memo값을 변경해준것은 아님. 
    #해결하려면 위 코드처럼 return값에 대한 결과를 출력하거나 n=0 or 1일때 return대신 memo에 저장하도록 해야함.