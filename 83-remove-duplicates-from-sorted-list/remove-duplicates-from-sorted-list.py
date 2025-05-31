# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        while temp:
            ptr = temp
            while ptr.next:
                if(ptr.next.val == temp.val):
                    ptr.next = ptr.next.next
                else:
                    ptr= ptr.next
            temp = temp.next
        return head
            
        