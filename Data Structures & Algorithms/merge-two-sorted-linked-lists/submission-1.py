class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode()
        dummy = head
        head1 = list1
        head2 = list2

        while head1 and head2 :

            if head1.val < head2.val:
                
                dummy.next = head1
                head1 = head1.next 
                dummy = dummy.next
            else:
                dummy.next = head2
                head2 = head2.next 
                dummy = dummy.next 

        if head1 :
            dummy.next = head1
        elif head2:
            dummy.next = head2

        return head.next                
                

            