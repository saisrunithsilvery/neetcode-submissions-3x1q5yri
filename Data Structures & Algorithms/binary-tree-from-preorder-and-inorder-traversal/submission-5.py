class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def solve(preorder, inorder):
            if not preorder:
                return None
            node = TreeNode(preorder[0])
            idx = inorder.index(preorder[0])
            node.left  = solve(preorder[1:1+idx], inorder[:idx])
            node.right = solve(preorder[1+idx:], inorder[idx+1:])
            return node
        return solve(preorder, inorder)