# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not inorder or not preorder:
            return None

        root = TreeNode(preorder[0])

        for i, val in enumerate(inorder):
            if val == preorder[0]:
                left_index = i
        root.left = self.buildTree(preorder[1:left_index+1], inorder[:left_index])
        root.right = self.buildTree(preorder[left_index+1:], inorder[left_index+1:])

        return root

        