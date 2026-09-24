# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:


        def bst(mini, maxi, node):
            if not node :
                return 0

            if  mini >= node.val or maxi <= node.val:
                return -1  

            
            
            x = bst(mini, node.val, node.left) 
            y = bst(node.val, maxi, node.right)

            if x == -1 or y == -1 :
                return -1
            else:
                return 0  

        return True if bst(float('-inf'), float('inf'), root) == 0 else False             









    
















        