# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if head.next is None: return False

        l1, l2 = head, head.next.next
        
        while l2 is not None:
            if l1.next == l2.next:
                return True
            l1, l2 = l1.next, l2.next.next
        return False
             
