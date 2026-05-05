# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        qu = deque()
        qu.append(root)

        if p.val > q.val:
            p, q = q, p

        while qu:

            curr = qu.popleft()

            val = curr.val

            if val >= p.val and val <= q.val:
                return curr

            if val < p.val and val < q.val :
                qu.append(curr.left)

            if val > p.val and val > q.val :
                qu.append(curr.left)    

