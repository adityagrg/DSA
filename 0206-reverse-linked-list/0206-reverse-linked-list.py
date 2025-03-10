# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # def util(self, head: ListNode, prev: ListNode):
    #     temp = head.next
    #     head.next = prev
    #     if temp == None:
    #         return head

    #     return self.util(temp, head)

    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if head == None or head.next == None:
    #         return head
        
    #     return self.util(head, None)
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        prev = None
        current = head

        while current != None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        
        return prev