# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        

        dummy = ListNode()
        dummy.next = head
        node = dummy
        node1 = dummy
        for _ in range(n):
            node1 = node1.next

        while node1.next:
            node1 = node1.next
            node = node.next

        
        node.next = node.next.next

        return dummy.next   



        