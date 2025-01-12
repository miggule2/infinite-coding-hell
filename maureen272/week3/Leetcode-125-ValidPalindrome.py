class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.upper())
        while len(strs) > 1:
            if strs.pop() != strs.pop(0): # pop()->마지막 요소 제거, pop(0)->첫번째 요소 제거
                return False
        return True
