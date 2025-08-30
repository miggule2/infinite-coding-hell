class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        def check(size): # size: 남은 바이트 수
            for i in range(start+1, start+size+1): # 다음 바이트 검사
                if i >= len(data) or (data[i] >> 6) != 0b10: # 2바이트 이상일 경우
                    return False
            return True

        start = 0 # 현재 바이트 위치
        while start < len(data): # 현재 바이트가 데이터의 길이보다 작을 때
            first = data[start]
            if (first >> 3) == 0b11110 and check(3): # 4바이트 문자일 경우 //0b11110을 하는 이유는 4바이트 문자의 첫 번째 바이트가 11110xxxx 형식이기 때문
                start += 4 # 4바이트를 모두 검사했으므로 4칸 이동
            elif (first >> 4) == 0b1110 and check(2):
                start += 3 # 3바이트를 모두 검사했으므로 3칸 이동
            elif (first >> 5) == 0b110 and check(1):
                start += 2 # 2바이트를 모두 검사했으므로 2칸 이동
            elif (first >> 7) == 0b0:
                start += 1 # 1바이트를 모두 검사했으므로 1칸 이동
            else:
                return False

        return True