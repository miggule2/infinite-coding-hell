class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 0, len(nums) # 초기화(red와 blue를 투포인터로 사용하고 중간에 white라는 포인터를 하나 더 사용)
        # red와 blue는 각각 오/왼으로 이동하면서 간격을 좁히고 white는 red와 blue 사이를 순회
        while white < blue: # white가 blue와 겹치면 비교 종료(왜냐면 이 상황에서 red는 1보다 작은 인덱스의 +1 지점, blue는 1보다 큰 인덱스의 첫지점을 가리킴)
            if nums[white] == 0: # 0이면 red와 white를 교체하고 값을 두개 다 증가
                nums[red], nums[white] = nums[white], nums[red]
                red += 1
                white += 1
            elif nums[white] > 1:
                blue -= 1
                nums[white], nums[blue] = nums[blue], nums[white]
            else:
                white += 1