# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTreeUtil(self, root: Optional[TreeNode]):
        if root == None:
            return root
        
        left = self.invertTreeUtil(root.left)
        right = self.invertTreeUtil(root.right)

        temp = root.left
        root.left = root.right
        root.right = temp
        del temp
        return root

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.invertTreeUtil(root)
        