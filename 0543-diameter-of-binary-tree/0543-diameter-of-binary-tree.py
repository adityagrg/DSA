# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def util(self, root, ans):
        if root is None:
            return 0

        left = self.util(root.left, ans)
        right = self.util(root.right, ans)

        if (left + right) > ans[0]:
            ans[0] = left + right

        return max(left, right) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = [0]
        self.util(root, ans)
        return ans[0]