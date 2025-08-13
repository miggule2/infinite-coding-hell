class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0 
        right = len(numbers) -1
        while left < right: 
            sum = numbers[left] + numbers[right] # 두 수의 합을 계산
            if sum < target:  # 합이 목표보다 작으면 왼쪽 포인터를 이동
                left += 1
            elif sum > target:  # 합이 목표보다 크면 오른쪽 포인터를 이동
                right -= 1
            else:  # 합이 목표와 같으면 결과 반환
                return left+1, right+1 # 
        