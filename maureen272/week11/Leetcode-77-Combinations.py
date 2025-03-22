class Solution(object):
    def combine(self, n, k):
        results = [] # store the final results
        def dfs(comb, start): 
            #base case
            if len(comb) == k: # 만약 comb의 길이가 k와 같다면, comb를 results에 추가하고 return
                results.append(comb[:]) # comb[:]를 해야지 comb의 reference가 아닌 값을 복사할 수 있음
                return

            for i in range(start, n+1): # start부터 n까지 반복
                comb.append(i) # comb에 i를 추가
                dfs(comb,i+1) # i+1부터 다시 dfs를 돌림
                comb.pop() # comb의 마지막 원소를 제거
            
        dfs([],1) # dfs를 호출
        return results
        #return list(itertools.combinations(range(1,n+1), k))