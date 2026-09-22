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
            return None

        result = []

        queue = deque()

        queue.append(root)

        while queue:

            length = len(queue)
            subset = []

            for _ in range(length):
                node = queue.popleft()
                subset.append(node.val)

            result.append(subset)    

        return result    

            

        


        