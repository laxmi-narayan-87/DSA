# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        l=r=c= float("-inf")
        if root.left: l=self.maxPathSum(root.left)
        if root.right: r=self.maxPathSum(root.right)
        c=root.val +self.pathsum(root.left) +self.pathsum(root.right)
        return max(l,r,c)
    
    def pathsum(self,root):
        if not root: return 0
        v= 0
        v=root.val+ max(self.pathsum(root.left),self.pathsum(root.right))
        if v<0: return 0
        return v