# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.sumOfNumbers(l1,l2,0)
        
    

    def sumOfNumbers(self,l1,l2,carry):
        if not l1 and not l2 and carry == 0:
            return None
        
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        total = val1 + val2 + carry
        node = ListNode(total % 10)
        new_carry = total // 10

        next1 =l1.next if l1 else 0
        next2 = l2.next if l2 else 0

        node.next =  self.sumOfNumbers(next1,next2,new_carry)
        return node





