# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        queue = deque([(root.left,root.right)])

        while queue:
            left, right = queue.popleft()
            
            if not left and not right:
                continue

            if left is None or right is None:
                return False
            
            if left.val != right.val:
                return False
            
            queue.append((left.left,right.right))
            queue.append((left.right,right.left))
        return True


