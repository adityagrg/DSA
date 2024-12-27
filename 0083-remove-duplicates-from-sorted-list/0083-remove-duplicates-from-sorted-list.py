# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        originalHead = head
        prev = head
        current = head.next

        while current != None:
            if current.val == prev.val:
                prev.next = current.next
                temp = current
                current = current.next
                del temp
            else:
                current = current.next
                prev = prev.next
        
        return originalHead