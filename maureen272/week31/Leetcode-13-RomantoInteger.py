class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        # 로마 숫자 각각의 값을 저장하는 딕셔너리
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0  # 최종 결과 값
        i = 0      # 현재 인덱스

        while i < len(s):
            # 현재 문자 값
            current = values[s[i]]

            # 다음 문자가 있고 현재 값이 다음 값보다 작은 경우 -> 빼기 규칙
            if i + 1 < len(s) and current < values[s[i + 1]]:
                # 다음 값에서 현재 값을 빼서 더함 (예: IV -> 5 - 1 = 4)
                total += values[s[i + 1]] - current
                i += 2  # 두 글자를 처리했으므로 2칸 이동
            else:
                # 일반적인 경우 -> 더하기
                total += current
                i += 1  # 한 글자만 처리했으므로 1칸 이동

        return total
