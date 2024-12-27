# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def util(self, root: Optional[TreeNode], level):
        if root == None:
            return level - 1

        return max(self.util(root.left, level + 1), self.util(root.right, level + 1))

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.util(root, 1)