# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # if root == None:
        #     return []
        
        # q1 = deque([root])
        # q2 = deque()
        # ans = []

        # current = []
        # while q1:
        #     element = q1.popleft()
        #     current.append(element.val)
        #     if element.left != None:
        #         q2.append(element.left)
        #     if element.right != None:
        #         q2.append(element.right)

        #     if not q1:
        #         q1, q2 = q2, q1
        #         ans.append(current)
        #         current = []

        # return ans
    
        if root == None:
            return []
        
        q = deque([root])
        ans = []

        while q:
            noOfElements = len(q)
            current = []
            for i in range(noOfElements):
                element = q.popleft()
                current.append(element.val)
                if element.left != None:
                    q.append(element.left)
                if element.right != None:
                    q.append(element.right)
            
            ans.append(current)
        
        return ans

