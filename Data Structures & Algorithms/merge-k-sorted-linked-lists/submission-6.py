# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
    
        # Step 1: Push head of each list
        # We use index `i` as tiebreaker because ListNode 
        # is not comparable
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val,i, node))
        
        dummy = ListNode(0)  # dummy head to simplify logic
        tail = dummy
        
        # Step 2: Always pick the smallest
        while heap:
            val, i, node = heapq.heappop(heap)  # pop min
            tail.next = node                      # add to result
            tail = tail.next
            
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        return dummy.next