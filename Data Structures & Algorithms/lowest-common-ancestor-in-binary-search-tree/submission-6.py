# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, P: TreeNode, q: 
        TreeNode) -> TreeNode:

        if not root :
            return None
            
        P = p.val
        Q = q.val
        if P > Q:
            P, Q = Q, P

        def solve(node1):
            if  P <= node1.val and node1.val <= Q :
                return node1

            elif node1.val > P and node1.val > Q :
                return solve(node1.left)
            else:
                return solve(node1.right)  
        return solve(root)






         

        