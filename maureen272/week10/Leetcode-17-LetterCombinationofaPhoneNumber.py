class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # 예외 처리
        if digits == "":
            return []
        # 숫자에 해당하는 문자들을 dictionary로 정의
        mapping = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        # 입력값을 리스트로 변환
        digits = list(digits)

        
        permutations = [] # 결과를 담을 리스트
        current_permutation = [] # 현재 순열을 담을 리스트

        #dfs
        def dfs(current_digit):
            if len(current_permutation) == len(digits): # 현재 순열의 길이가 입력값의 길이와 같다면
                permutations.append("".join(current_permutation)) # 결과 리스트에 추가
                return
            
            next_digits = list(mapping[int(digits[current_digit])]) # 다음 숫자에 해당하는 문자들을 리스트로 변환
            for i in range(len(next_digits)):# 다음 숫자에 해당하는 문자들을 순회
                next_digit = next_digits[i]
                current_permutation.append(next_digit)
                dfs(current_digit + 1)# 다음 숫자로 넘어감
                current_permutation.pop()# 현재 순열에서 제거
        dfs(0)
        return permutations