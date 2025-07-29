# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
        

        # while current:
        #     if current.val == node.val:
        #         current.next = current.next.next
        #         current = current.next
        #     current = current.next
        # return current.next
        