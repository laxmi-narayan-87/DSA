# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        l=r=c=0
        if (root.left): l=self.longestUnivaluePath(root.left)
        if root.right: r=self.longestUnivaluePath(root.right)
        if root.left and root.left.val==root.val: c+=1+self.height(root.left)
        if root.right and root.right.val== root.val: c+=1+self.height(root.right)
        return max(l,r,c)
    
    def height(self,root):
        if not root: return 0
        l=r=0
        if root.left and root.left.val==root.val: l=1+self.height(root.left)
        if root.right and root.right.val==root.val: r=1+self.height(root.right)
        if l==0 and r==0: return 0
        return max(l,r)