from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0

    def canTransform(word1, word2):
        diff_count = sum(1 for a, b in zip(word1, word2) if a != b)
        return diff_count == 1

    # BFS
    queue = deque([(begin, 0)])
    visited = set()

    while queue:
        current_word, steps = queue.popleft()

        if current_word == target: 
            return steps

        for word in words:
            if word not in visited and canTransform(current_word, word):
                visited.add(word)
                queue.append((word, steps + 1))

    return 0
