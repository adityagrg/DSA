# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def util(self, root: Optional[TreeNode]):
        if root == None:
            return 0

        left = self.util(root.left)
        right = self.util(root.right)

        return max(left, right) + 1

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.util(root)

    