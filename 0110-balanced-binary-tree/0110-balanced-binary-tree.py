# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def util(self, root) -> Optional[int]:
        if root == None:
            return 0
        
        hLeft = self.util(root.left)
        if hLeft is None:
            return None
        hRight = self.util(root.right)
        if hRight is None:
            return None

        if abs(hRight - hLeft) <= 1:
            return max(hLeft, hRight) + 1
        else:
            return None

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if self.util(root) is None:
            return False
        else:
            return True