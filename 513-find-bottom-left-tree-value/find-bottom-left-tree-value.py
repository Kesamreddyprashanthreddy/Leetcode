# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        result = root.val
        while q:
            for i in range(len(q)):
                curr = q.popleft()
                if i == 0:
                    result = curr.val
                
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        return result
        
