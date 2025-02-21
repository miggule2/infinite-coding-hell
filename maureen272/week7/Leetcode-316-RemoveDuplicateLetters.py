class Solution(object):
    def removeDuplicateLetters(self, s):
        count = {char: s.count(char) for char in set(s)}
        
        stack = []  
        in_stack = set()  
        
        for char in s:
            count[char] -= 1  
            if char in in_stack:
                continue  
            
            while stack and char < stack[-1] and count[stack[-1]] > 0:
                removed = stack.pop()
                in_stack.remove(removed)
            
            stack.append(char)
            in_stack.add(char)
        
        return ''.join(stack)


        