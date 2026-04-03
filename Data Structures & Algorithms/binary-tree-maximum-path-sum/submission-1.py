class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val  # global max

        def dfs(node):
            if not node:
                return 0

            # get best path from each subtree, ignore negatives
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            # path that "splits" at this node (left -> node -> right)
            self.res = max(self.res, node.val + left + right)

            # return best single branch to parent (can't split)
            return node.val + max(left, right)

        dfs(root)
        return self.res