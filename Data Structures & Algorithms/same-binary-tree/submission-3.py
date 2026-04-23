class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(a, b):

            if not a and not b:
                return 0

            elif not a or not b:
                return -1

            elif a.val == b.val:
                left = dfs(a.left, b.left)
                right = dfs(a.right, b.right)   # ✅ fixed

                if left == 0 and right == 0:
                    return 0
                else:
                    return -1

            else:
                return -1

        return dfs(p, q) == 0