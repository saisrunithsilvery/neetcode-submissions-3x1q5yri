# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        q =deque()


        q.append(root)
        result =[]
        while q:

            z=[]
            lenq = len(q)
            for _ in range(0, lenq):

                x = q.popleft()
                z.append(x.val)
                if x.left :
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
            result.append(z)            

        return result    

                
        