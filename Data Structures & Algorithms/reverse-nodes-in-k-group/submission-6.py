from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k <= 1:
            return head

        # 1) Compute length
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next

        groups = n // k  # number of full k-sized groups

        dummy = ListNode(0, head)
        groupPrev = dummy

        # Helper: reverse exactly k nodes after groupPrev, return new tail (old head)
        for _ in range(groups):
            # groupPrev -> a -> b -> ... (k nodes) -> groupNext
            prev = None
            cur = groupPrev.next          # first node of this group (will become tail)
            tail = cur

            # Reverse k nodes
            for _ in range(k):
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt

            # Now:
            # prev = new head of reversed group
            # cur  = node after the group (groupNext)
            

            # Reconnect
            groupPrev.next = prev
            tail.next = cur

            # Move groupPrev to tail for next iteration
            groupPrev = tail

        return dummy.next