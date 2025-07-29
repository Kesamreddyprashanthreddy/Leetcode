# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        sum_of_nodes = {}
        prefix_sum = 0
        current = dummy
        while current:
            prefix_sum += current.val
            sum_of_nodes[prefix_sum] = current
            current = current.next
        
        prefix_sum = 0
        current = dummy
        while current:
            prefix_sum += current.val
            current.next = sum_of_nodes[prefix_sum].next
            current = current.next
        return dummy.next

            

