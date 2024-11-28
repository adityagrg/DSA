# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def util(self, prev, head):
        if head == None:
            return prev

        temp = head.next
        head.next = prev
        return self.util(head, temp)

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        temp = head.next
        head.next = None
        return self.util(head, temp)