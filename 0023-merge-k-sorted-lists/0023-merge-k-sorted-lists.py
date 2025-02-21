# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lists = [x for x in lists if x != None]
        if len(lists) == 0:
            return None

        head = ListNode()
        current = head

        while len(lists) != 0:
            if len(lists) == 1:
                current.next = lists[0]
                return head.next

            minVal = float('inf')
            minPointer = lists[0]
            indexMin = 0
            for index in range(0, len(lists)):
                currentList = lists[index]
                if currentList.val < minPointer.val:
                    minPointer = currentList
                    indexMin = index
            
            current.next = minPointer
            lists[indexMin] = minPointer.next
            current = current.next
            current.next = None
            if lists[indexMin] == None:
                del lists[indexMin]
        
        return head.next