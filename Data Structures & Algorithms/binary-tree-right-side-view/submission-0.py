# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        q = deque()    
        
        q.append(root)
        result =[]
        while q:

            lenq = len(q)

            for i in range(0, lenq):
                x = q.popleft()

                if x.left:
                    q.append(x.left)

                if x.right:
                    q.append(x.right)                        

                if i == lenq-1 :
                    result.append(x.val)

        return result            
