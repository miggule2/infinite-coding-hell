from functools import cmp_to_key

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # 비교 함수 정의
        # 두 숫자 x, y를 문자열로 변환하여 x+y와 y+x을 비교
        def compare(x, y):
            if x + y > y + x: # x가 앞에 오는 것이 더 크면 -1
                return -1
            elif x + y < y + x: # y가 앞에 오는 것이 더 크면 1
                return 1
            else: # 같으면 0
                return 0
        
        # 숫자를 문자열로 변환
        nums_str = list(map(str, nums))
        # 정렬
        nums_str.sort(key=cmp_to_key(compare))
        
        # "0000..." 같은 경우 "0"으로
        if nums_str[0] == '0':
            return '0'
        
        return ''.join(nums_str)
