# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not preorder or not inorder:
            return None
        
        root_val = preorder[0]
        root = TreeNode(root_val)
        
        root_index_in_inorder = inorder.index(root_val)
        # 주석 한국어로 달아줘
        # 루트 노드의 인덱스를 inorder에서 찾기
        left_inorder = inorder[:root_index_in_inorder] # 왼쪽 서브트리의 inorder
        right_inorder = inorder[root_index_in_inorder + 1:] # 오른쪽 서브트리의 inorder
        
        # 왼쪽 서브트리의 preorder는 루트 노드 다음부터 왼쪽 inorder의 길이만큼
        left_preorder = preorder[1:1 + len(left_inorder)] 
        right_preorder = preorder[1 + len(left_inorder):]
        
        root.left = self.buildTree(left_preorder, left_inorder) # 왼쪽 서브트리의 트리 생성
        root.right = self.buildTree(right_preorder, right_inorder) # 오른쪽 서브트리의 트리 생성
        
        return root