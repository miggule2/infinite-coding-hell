class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.output = [] 
        self.backtrack(0, [], nums) 
        return self.output
    def backtrack(self, first, curr, nums): # first: 시작 index, curr: 현재까지의 subset, nums: 전체 리스트
        self.output.append(curr[:]) # 현재까지의 subset을 output에 추가
        for i in range(first, len(nums)): # first부터 nums의 길이까지 반복
            new_curr = curr.copy() # curr의 복사본을 new_curr에 저장
            new_curr.append(nums[i]) # new_curr에 nums[i]를 추가
            self.backtrack(i+1, new_curr, nums) # i+1부터 다시 backtrack을 돌림