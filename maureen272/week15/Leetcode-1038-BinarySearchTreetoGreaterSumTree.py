# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.sum = 0  # 누적 합을 저장할 변수

        def traverse(node): # 중위 순회
            if not node:
                return
            # 오른쪽부터 방문
            traverse(node.right)
            # 현재 노드 처리
            self.sum += node.val # 현재 노드의 값을 누적 합에 더함
            node.val = self.sum # 현재 노드의 값을 누적 합으로 업데이트
            # 왼쪽 방문
            traverse(node.left)

        traverse(root)
        return root