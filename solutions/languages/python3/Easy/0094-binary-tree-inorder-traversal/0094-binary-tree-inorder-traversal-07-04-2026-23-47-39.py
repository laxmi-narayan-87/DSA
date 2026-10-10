# Definition for a binaAAry tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack=[]
        if not root:
            return []
        def inorder(node):
            if not node:
                return 
            inorder(node.left)
            stack.append(node.val)
            inorder(node.right)
        inorder(root)
        return stack