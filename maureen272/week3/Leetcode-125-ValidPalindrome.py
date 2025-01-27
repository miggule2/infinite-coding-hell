#solution 1 : 리스트로 변환
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

# solution 2 : 데크 자료형을 이용한 최적화
# Deque는 스택과 큐의 기능을 모두 가진 객체로 출입구가 양쪽에 있는 큐
# Deque는 리스트에 비해 효율적인 자료 저장 방식을 제공
# 리스트의 pop(0)은 O(n)인데 반해 데크의 popleft()는 O(1)임

    def isPalindrome(self, s):
        strs = collections.deque()
        for char in s:
            if char.isalnum():
                strs.append(char.upper())
        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False    
        return True
    
# solution 3 : 슬라이싱 사용
class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s) # 정규식으로 영문자, 숫자가 아닌 문자를 제거
        return s == s[::-1] # 슬라이싱을 이용용