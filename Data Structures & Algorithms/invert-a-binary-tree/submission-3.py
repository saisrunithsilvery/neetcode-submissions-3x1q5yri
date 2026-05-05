# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root :
            return root

        q = deque()

        q.append(root)
        while q:
            x = q.popleft()

            if x.left and x.right :
                x.left, x.right = x.right, x.left
                q.append(x.left)
                q.append(x.right)

            elif x.left :
                x.right = x.left
                q.append(x.right)

            elif x.right :
                x.left = x.right     
                q.append(x.left)      

        return root         
        