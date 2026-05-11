# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # Get length of head
        c = 0
        tmp = head
        while tmp:
            c += 1
            tmp = tmp.next
        pos = c - n

        if pos == 0: return head.next

        # Traverse until we find the index position same as pos
        tmp = head
        for i in range(c - 1):
            if (i + 1) == pos:
                tmp.next = tmp.next.next
                break
            tmp = tmp.next
        return head
        
        