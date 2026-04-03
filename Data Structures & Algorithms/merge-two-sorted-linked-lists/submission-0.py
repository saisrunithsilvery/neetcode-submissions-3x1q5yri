# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(-1)
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1      # reuse node
                list1 = list1.next
            else:
                tail.next = list2      # reuse node
                list2 = list2.next
            tail = tail.next           # move tail forward

        # attach the remaining nodes
        tail.next = list1 if list1 else list2

        return dummy.next