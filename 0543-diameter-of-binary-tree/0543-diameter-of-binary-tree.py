# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = 0
    def util(self, root):
        if root is None:
            return 0

        left = self.util(root.left)
        right = self.util(root.right)

        if (left + right) > self.ans:
            self.ans = left + right

        return max(left, right) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.util(root)
        return self.ans