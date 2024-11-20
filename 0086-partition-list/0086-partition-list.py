# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head
        new_list = ListNode()
        first_head = new_list

        while head and head.val < x:
            new_list.next = head
            head = head.next
            new_list = new_list.next
        
        new_list.next = None

        second_head = head
        if head != None:
            prev = second_head
            head = head.next
            while head != None:
                if head.val < x:
                    temp = head.next
                    prev.next = temp
                    new_list.next = head
                    head = prev.next
                    new_list = new_list.next
                    new_list.next = None
                else:
                    prev = head
                    head = head.next
        
        new_list.next = second_head
        return first_head.next