# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        index = {val: i for i, val in enumerate(inorder)}
        def dfs(left, right):
            if left > right:
                return None
            root_val = postorder.pop()
            root = TreeNode(root_val)
            mid = index[root_val]
            root.right = dfs(mid + 1, right)
            root.left = dfs(left, mid - 1)
            return root
        return dfs(0, len(inorder) - 1)