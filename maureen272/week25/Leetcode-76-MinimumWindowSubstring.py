class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need = collections.Counter(t) # t에 필요한 문자 개수
        missing = len(t) # 필요한 문자의 전체 개수
        left = start = end = 0 

        # 오른쪽 포인터 이동
        for right, char in enumerate(s,1): # right는 1부터 시작 ->  ennumerate(s,1)은 1부터 시작한다는 의미
            # 필요 문자 개수 감소
            missing -= need[char] > 0 # 필요 문자가 있으면 missing 감소
            need[char] -= 1 

            # 필요 문자가 0이면(missing==0) 왼쪽 포인터 이동 판단
            if missing == 0: 
                while left < right and need[s[left]] < 0: # 왼쪽 포인터가 불필요한 문자를 가리키면 값이 음수일 것임
                    need[s[left]] += 1
                    left += 1

                if not end or right - left <= end - start: # 최소 길이 갱신
                    start, end = left, right # end는 right + 1
                # missing이 0이 될때까지의 오른쪽 포인터와 need[s[left]]가 0이 될 때까지의 왼쪽 포인터를 정답으로 간주하고
                # 이 값이 더 작은 값을 찾을 때까지 유지하다, 가장 작은 값의 경우 그 값을 리턴