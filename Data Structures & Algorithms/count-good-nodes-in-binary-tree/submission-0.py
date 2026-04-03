# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root :
            return 0

        self.count = 0
        maxnum= root.val

        def dfs(root, maxnum):

            if root.val >= maxnum:
                print(root.val)
                self.count +=1
            
            if root.left:
                dfs(root.left, max(root.val, maxnum))
            if root.right:
                dfs(root.right, max(root.val, maxnum))

            return
        dfs(root, maxnum)
        return self.count