class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None

        # Pass 1: create copies beside originals
        cur = head

        while cur:
            copy = Node(cur.val)

            copy.next = cur.next
            cur.next = copy

            cur = copy.next

        # Pass 2: assign random pointers
        cur = head

        while cur:
            copy = cur.next

            if cur.random:
                copy.random = cur.random.next

            cur = copy.next

        # Pass 3: separate the two lists
        cur = head
        copy_head = head.next

        while cur:
            copy = cur.next

            cur.next = copy.next

            if copy.next:
                copy.next = copy.next.next

            cur = cur.next

        return copy_head