# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        current = head
        while current:
            count += 1 
            current = current.next

        if count == 1:
            return 
        

        current = head
        if count == n:
            return head.next
        index = 1
        while current and  current.next:  
            if index == count - n:
                current.next = current.next.next
            index += 1
            current = current.next

        return head

        