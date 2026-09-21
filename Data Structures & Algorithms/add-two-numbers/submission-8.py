# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        head1 = l1
        head2 = l2
        carry = 0
        result = ListNode()
        node = result
        

        while head1 or head2 or carry :

            x = head1.val if head1 else 0
            y = head2.val if head2 else 0

            value = (x+y+carry) % 10
            carry = (x+y+carry)//10

            dummy = ListNode(value)
            node.next = dummy
            node = node.next
            head1 = head1.next if head1 else 0
            head2 = head2.next if head2 else 0

        return result.next    



            



        




            


        