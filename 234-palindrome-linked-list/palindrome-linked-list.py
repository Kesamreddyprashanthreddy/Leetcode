# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.first = head
        return self.palindrome(head)
    
    def palindrome(self,current):
        if current is None:
            return True
        
        result = self.palindrome(current.next)

        if result == False:
            return False
        
        res = self.first.val == current.val
        self.first = self.first.next
        return res
        