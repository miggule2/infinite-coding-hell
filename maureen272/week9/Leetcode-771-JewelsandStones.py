class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        alpha = {} # dictionary to store the frequency of each stone
        
        for i in stones: # count the frequency of each stone
            if i not in alpha: # if the stone is not in the dictionary, add it
                alpha[i] = 1 
            else: # if the stone is in the dictionary, increment the frequency
                alpha[i] += 1
        
        cnt = 0
        for j in jewels: # count the number of jewels
            if j in alpha:
                cnt += alpha[j]
        
        return cnt # return the number of jewels