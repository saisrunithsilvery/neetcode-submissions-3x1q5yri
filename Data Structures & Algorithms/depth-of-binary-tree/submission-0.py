# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def max1(node, count):

            if not node:
                return count

            count +=1

            return max( max1(node.right, count), max1(node.left, count))
        return max1(root, 0)        
        