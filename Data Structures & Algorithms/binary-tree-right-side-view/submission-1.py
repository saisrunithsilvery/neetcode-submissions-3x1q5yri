# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []
        result = []
        q = deque()

        q.append(root)

        while q:

            leng = len(q)
            for i in range(leng):
                x = q.popleft()
                if i == leng-1:
                    result.append(x.val)

                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
        return result                    




        