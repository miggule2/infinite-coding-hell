import collections
import re

class Solution(object):
#solution1: 내가 짠 코드
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        # 문장을 소문자로 변환
        paragraph = paragraph.lower()
        
        # 구두점을 공백으로 대체
        for char in "!?',;.":
            paragraph = paragraph.replace(char, " ")
        
        # 공백을 기준으로 단어 나누기
        words = paragraph.split()
        
        # 금지된 단어를 제외한 단어의 빈도를 카운트
        banned_set = set(banned)
        word_count = collections.Counter(word for word in words if word not in banned_set)
        
        return word_count.most_common(1)[0][0]

#solution2: 리스트 컴프리헨션과 Counter 객체를 이용
    def mostCommonWord(self, paragraph, banned):
        # 정규식으로 문자가 아닌 것은 공백으로 치환
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
        counts = collections.Counter(words)
        # 가장 흔하게 등장하는 단어의 첫 번째 인덱스 리턴
        return counts.most_common(1)[0][0]
    
# 정규식이란?
# 정규식(Regular Expression)은 특정한 규칙을 가진 문자열의 집합을 표현하는 데 사용하는 형식 언어
# 파이썬에서는 re 모듈을 사용하여 정규식을 지원
# re.sub(pattern, repl, string)은 string에서 pattern과 매치하는 텍스트를 repl로 치환
# r'[^\w]'는 \w(단어 문자)가 아닌 문자를 의미
# 정규식에서 []는 문자 집합을 나타내며 ^은 not을 의미

# 정규식 sub메소드는?
# re.sub(pattern, repl, string) : string에서 pattern과 매치하는 텍스트를 repl로 치환

