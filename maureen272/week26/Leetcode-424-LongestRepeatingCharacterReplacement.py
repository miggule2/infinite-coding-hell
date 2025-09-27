import collections

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left = 0 
        right = 0
        counts = collections.Counter()
        for right in range(1, len(s)+1): # s[right-1]에 접근하기 위해서 right는 1부터 시작
            counts[s[right-1]] += 1 # s[right-1] 문자를 추가
            max_count = max(counts.values()) # 가장 많이 등장한 문자의 개수
            # 현재 윈도우 크기 - 가장 많이 등장한 문자의 개수 > k 이면, k번 이상 문자를 바꿔야 하므로 left를 옮김
            if (right - left) - max_count > k:
                counts[s[left]] -= 1 # left 문자를 제거
                left += 1 # left 포인터를 오른쪽으로 한 칸 이동
        return right - left # 최대 길이 반환
