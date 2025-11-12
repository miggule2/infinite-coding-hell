class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """

        # 두 리스트(left, right)의 가능한 모든 조합에 대해 연산 수행
        def compute(left, right, op):
            results = [] 
            for l in left:
                for r in right:
                    if op == '+':
                        results.append(l + r)  # 덧셈 결과 추가
                    elif op == '-':
                        results.append(l - r)  # 뺄셈 결과 추가
                    elif op == '*':
                        results.append(l * r)  # 곱셈 결과 추가
            return results  # 가능한 모든 결과 리스트 반환

        # expression이 숫자만으로 이루어진 경우
        if expression.isdigit():
            return [int(expression)]  # 숫자로 변환해 리스트로 반환

        results = []  # 가능한 모든 결과 저장용 리스트
        # expression의 각 문자 순회
        for idx, value in enumerate(expression):
            # 연산자(+, -, *)인 경우
            if value in "-+*":
                # 연산자를 기준으로 왼쪽, 오른쪽 부분식 분할
                left = self.diffWaysToCompute(expression[:idx])
                right = self.diffWaysToCompute(expression[idx+1:])
                
                # 왼쪽과 오른쪽의 가능한 결과 조합을 계산해 results에 추가
                results.extend(compute(left, right, value))
                
        return results  # 모든 가능한 결과 반환
