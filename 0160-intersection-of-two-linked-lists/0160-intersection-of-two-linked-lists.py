# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        headATemp = headA
        headBTemp = headB

        countA = 0
        while headATemp != None:
            countA += 1
            headATemp = headATemp.next
        
        countB = 0
        while headBTemp != None:
            countB += 1
            headBTemp = headBTemp.next
        
        headATemp = headA
        headBTemp = headB
        if countA > countB:
            extra = countA - countB
            for i in range(0, extra):
                headATemp = headATemp.next
        
        if countB > countA:
            extra = countB - countA
            for i in range(0, extra):
                headBTemp = headBTemp.next

        while headATemp != None and headATemp != headBTemp:
            headATemp = headATemp.next
            headBTemp = headBTemp.next
        
        if headATemp != None:
            return headATemp
        else:
            return None