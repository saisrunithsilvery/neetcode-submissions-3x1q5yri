# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        result = []

        if not root:
            return []

        q = deque()

        q.append(root)

        while q:
            temp = []
            x = len(q)
            for i in range(x):
                node = q.popleft()
                a = node.val
                temp.append(a)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(temp)

        return result            




        