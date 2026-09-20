# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head or head.next == None:
            return None

        node1 = ListNode()
        node1.next = head
        for _ in range(n):
            node1 = node1.next

        node = ListNode()
        node.next = head
        while node1.next:
            node1 = node1.next
            node = node.next

        
        node.next = node.next.next

        return head    



        