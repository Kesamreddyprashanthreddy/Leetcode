# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        q = deque([root])
        res = []
        while q:
            l = []
            for _ in range(len(q)):
                node = q.popleft()
                l.append(node)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(l)
        return len(res)



