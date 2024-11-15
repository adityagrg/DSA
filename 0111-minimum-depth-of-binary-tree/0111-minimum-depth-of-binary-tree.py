# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _util(self, root, level):
        if root.left == None and root.right == None:
            return level
        
        min1 = min2 = float('inf')
        if root.left != None:
            min1 = self._util(root.left, level + 1)
        
        if root.right != None:
            min2 = self._util(root.right, level + 1)

        return min(min1, min2)

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        return self._util(root, 1)