# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newList = ListNode()
        newListPointer = newList

        ptr1 = list1
        ptr2 = list2
        while ptr1 != None and ptr2 != None:
            if ptr1.val < ptr2.val:
                newListPointer.next = ptr1
                ptr1 = ptr1.next
                newListPointer = newListPointer.next
                newListPointer.next = None
            else:
                newListPointer.next = ptr2
                ptr2 = ptr2.next
                newListPointer = newListPointer.next
                newListPointer.next = None

        if ptr1 != None:
            newListPointer.next = ptr1
        
        if ptr2 != None:
            newListPointer.next = ptr2

        return newList.next