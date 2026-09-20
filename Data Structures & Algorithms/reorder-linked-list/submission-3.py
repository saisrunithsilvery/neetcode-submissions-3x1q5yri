# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow = head 
        fast = head 

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

        start = slow.next
        slow.next = None
        prev = None
        while start :
            temp = start.next
            start.next = prev
            prev = start
            start = temp

        head2 = prev


        while head2:
            temp1 = head.next
            temp2 = head2.next

            head.next = head2
            head2.next = temp1

            head = temp1
            head2 = temp2

        

        


        