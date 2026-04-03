from collections import deque

class Codec:

    def serialize(self, root):
        if not root:
            return "N"
        res = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if not node:
                res.append("N")
            else:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)

        return ",".join(res)

    def deserialize(self, data):
        vals = data.split(",")
        if vals[0] == "N":
            return None

        root = TreeNode(int(vals[0]))
        queue = deque([root])
        i = 1

        while queue:
            node = queue.popleft()

            # left child
            if vals[i] != "N":
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1

            # right child
            if vals[i] != "N":
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1

        return root