class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # 1. 두 숫자의 비트가 다른 위치를 찾기 위해 XOR 연산을 수행
        xor_result = x ^ y

        # 2. 다른 비트의 개수(해밍 거리)를 저장할 변수를 초기화
        distance = 0
        
        # 3. xor_result의 모든 비트를 확인할 때까지 반복
        # 숫자가 0이 되면 더 이상 1인 비트가 없다는 의미임
        while xor_result > 0:
            # 마지막 비트가 1인지 확인
            if (xor_result & 1) == 1:
                distance += 1
            
            # 5. 오른쪽으로 한 칸 비트 쉬프트하여 다음 비트를 검사할 준비하기
            xor_result >>= 1
            
        return distance
    
        # return bin(x^y).count('1') -> 한 줄 풀이
        