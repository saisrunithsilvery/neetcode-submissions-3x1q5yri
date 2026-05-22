# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    from collections import deque

    def invertTree(self, root):
        if not root:
            return None
        
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            
            # swap children
            node.left, node.right = node.right, node.left
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return root

                        

        