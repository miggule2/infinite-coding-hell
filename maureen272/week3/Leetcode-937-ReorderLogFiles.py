class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0])) # 정렬은 식별자를 제외한 문자열 [1:]을 기준으로 하고 이것이 동일할 경우 후순위로 식별자 [0]로 정렬

        return letters + digits # 문자로 구성된 로그가 숫자보다 앞에 와야하고 숫자로그는 입력 순서대로 하기때문에 정렬을 다시 해줄 필요x