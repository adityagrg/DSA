# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildPath(self, root, nodeToBeFound, path: list):
        if root == None:
            return False

        path.append(root)
        if root == nodeToBeFound:
            return True
        
        if self.buildPath(root.left, nodeToBeFound, path):
            return True

        if self.buildPath(root.right, nodeToBeFound, path):
            return True
        
        path.pop()
        return False

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        firstPath = []
        self.buildPath(root, p, firstPath)

        secondPath = []
        self.buildPath(root, q, secondPath)

        i = 0
        while i < len(firstPath) and i < len(secondPath) and firstPath[i] == secondPath[i]:
            i += 1
            continue
        
        if i == len(firstPath):
            return firstPath[-1]
        
        if i == len(secondPath):
            return secondPath[-1]
        
        return secondPath[i - 1]