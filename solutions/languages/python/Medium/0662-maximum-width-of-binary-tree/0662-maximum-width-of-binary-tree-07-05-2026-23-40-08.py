# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([(root, 0)])
        ans = 0
        while q:
            n = len(q)
            first = q[0][1]
            last = first
            for _ in range(n):
                node, idx = q.popleft()
                idx -= first         
                last = idx
                if node.left:
                    q.append((node.left, 2 * idx + 1))
                if node.right:
                    q.append((node.right, 2 * idx + 2))
            ans = max(ans, last + 1)
        return ans