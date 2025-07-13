import collections

# 트라이의 노드
class TrieNode:
    def __init__(self):
        self.word = False # 단어의 끝을 표시하기 위한 플래그
        self.children = collections.defaultdict(TrieNode) # 자식 노드를 저장하기 위한 딕셔너리

class Trie(object):
    def __init__(self):
        self.root = TrieNode() # 트라이의 루트 노드 초기화

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root # 루트 노드에서 시작
        for char in word: # 단어의 각 문자에 대해
            node = node.children[char] # 해당 문자의 자식 노드로 이동 (없으면 새로 생성)
        node.word = True # 단어의 끝을 표시하기 위해 플래그 설정
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node = self.root # 루트 노드에서 시작
        for char in word:
            if char not in node.children: # 해당 문자가 자식 노드에 없으면
                return False # 단어가 존재하지 않음
            node = node.children[char] # 해당 문자의 자식 노드로 이동
        return node.word
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        node = self.root 
        for char in prefix:
            if char not in node.children: # 해당 문자가 자식 노드에 없으면
                return False 
            node = node.children[char] # 해당 문자의 자식 노드로 이동
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)