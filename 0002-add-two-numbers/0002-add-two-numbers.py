# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        ans = head
        carry = 0

        while l1 != None and l2 != None:
            valToBeAdded = (l1.val + l2.val + carry) % 10
            carry = (l1.val + l2.val + carry) // 10
            ans.next = ListNode(valToBeAdded)
            ans = ans.next
            l1 = l1.next
            l2 = l2.next
        
        while l1 != None:
            valToBeAdded = (l1.val + carry) % 10
            carry = (l1.val + carry) // 10
            ans.next = ListNode(valToBeAdded)
            ans = ans.next
            l1 = l1.next
        
        while l2 != None:
            valToBeAdded = (l2.val + carry) % 10
            carry = (l2.val + carry) // 10
            ans.next = ListNode(valToBeAdded)
            ans = ans.next
            l2 = l2.next
        
        if carry != 0:
            ans.next = ListNode(1)
        
        return head.next

