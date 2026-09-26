# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        data = []
       
        def dfs(node):
            if not node:
                data.append("N")
                return

            data.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return ",".join(data) 

        

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        list1 = data.split(",")
        l = 0
        def solve():
            nonlocal l
            if l == len(list1):
                return 

            if list1[l] =='N':
                l +=1
                return None    

            node = TreeNode(list1[l])
            l +=1
            node.left = solve()
            node.right = solve()

            return node
        return solve()     







        
