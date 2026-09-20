# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None

        # original node -> copied node
        deep_copy = {None: None}

        dummy = head

        # Pass 1: create all copied nodes
        while dummy:
            deep_copy[dummy] = Node(dummy.val)
            dummy = dummy.next

        dummy = head

        # Pass 2: connect next and random pointers
        while dummy:
            deep_copy[dummy].next = deep_copy[dummy.next]
            deep_copy[dummy].random = deep_copy[dummy.random]

            dummy = dummy.next

        return deep_copy[head]