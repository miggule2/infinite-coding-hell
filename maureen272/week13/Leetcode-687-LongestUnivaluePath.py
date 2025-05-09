# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.longest = 0

        def dfs(node):
            if node is None:
                return 0
            
            # backtracking으로 경로를 찾아야하기 때문에 재귀탐색 써서 leaf노드부터 시작할 수 있게함
            left = dfs(node.left)
            right = dfs(node.right)

            left_path = right_path = 0

            # node.left가 None일 수 있는데, 이 경우 node.left.val에 접근하면 AttributeError가 발생함
            # 그렇기 때문에 node.left를 해줘야 함
            if node.left and node.left.val == node.val:
                left_path = left + 1
            if node.right and node.right.val == node.val:
                right_path = right + 1

            # 양쪽 길이의 합이 현재 노드를 지나가는 경로의 최대 길이
            self.longest = max(self.longest, left_path + right_path)

            # 부모에게 반환할 때는 한 방향만 (왼쪽 or 오른쪽) 최대값만 반환
            return max(left_path, right_path)

        dfs(root)
        return self.longest
