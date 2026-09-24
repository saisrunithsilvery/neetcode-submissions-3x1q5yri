class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx_map = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0

        def solve(left, right):
            if left > right:
                return None
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            node = TreeNode(root_val)
            mid = idx_map[root_val]
            node.left  = solve(left, mid - 1)   # must build left before right
            node.right = solve(mid + 1, right)
            return node

        return solve(0, len(inorder) - 1)