class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1 # 초깃값 설정
        
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target: # 타겟을 찾은 경우
                return mid

            # 어떤 절반이 정렬되어 있는지 확인
            if nums[left] <= nums[mid]:  # 왼쪽 절반이 정렬되어 있는 경우
                if nums[left] <= target < nums[mid]: # 타겟이 왼쪽 절반에 있는 경우
                    right = mid - 1  
                else:
                    left = mid + 1   # 타겟이 오른쪽 절반에 있는 경우
            else:  # 오른쪽 절반이 정렬되어 있는 경우
                if nums[mid] < target <= nums[right]: # 타겟이 오른쪽 절반에 있는 경우
                    left = mid + 1   
                else:
                    right = mid - 1  # 타겟이 왼쪽 절반에 있는 경우

        return -1  # 타겟을 찾지 못한 경우