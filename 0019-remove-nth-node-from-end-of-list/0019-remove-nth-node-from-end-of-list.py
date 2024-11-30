# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        m = 0
        temp = head

        while temp != None:
            m += 1
            temp = temp.next
        
        if m == 1:
            return None
        
        if m == n:
            return head.next
        
        getValAt = m - n
        
        prev = head
        temp = head.next
        for i in range(1, getValAt):
            prev = temp
            temp = temp.next
        
        prev.next = temp.next
        del temp

        return head