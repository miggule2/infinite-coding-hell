class Solution(object):
    # solution 1: 브루트포스로 계산
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
    # solution 2: in을 이용한 탐색(target - n이 nums에 있는지 확인)  
    def twoSum(self, nums, target):
        for i, n in enumerate(nums):
            complement = target - n
            if complement in nums[i+1:]:
                return [i, nums[i+1:].index(complement) + (i+1)]
    # solution 3: 딕셔너리 이용
    def twoSum(self, nums, target):
        nums_map = {}
        for i, num in enumerate(nums):
            nums_map[num] = i
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return [i, nums_map[target - num]]
            
    # solution 4: 딕셔너리 이용(한번에)
    def twoSum(self, nums, target):
        nums_map = {}
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target - num], i]
            nums_map[num] = i
