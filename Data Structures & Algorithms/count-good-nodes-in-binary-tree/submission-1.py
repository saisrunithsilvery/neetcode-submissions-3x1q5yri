# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        self.count = 0

        val = root.val

        def dfs(node, val):

            if node.val >= val:
                self.count +=1

            val = max(val, node.val)
            if node.left:
                dfs(node.left, val)
            if node.right:
                dfs(node.right, val)

        dfs(root, val)
        return self.count                
    
        