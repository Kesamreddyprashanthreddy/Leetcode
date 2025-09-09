# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        d = {}
        children = set()

        for parent,child,isLeft in descriptions:
            if parent not in d:
                d[parent] = TreeNode(parent)
            if child not in d:
                d[child] = TreeNode(child)
            
            if isLeft == 1:
                d[parent].left = d[child]
            if isLeft == 0:
                d[parent].right = d[child]
            
            children.add(child)
        
        for val in d:
            if val not in children:
                return d[val]
        return None
            



