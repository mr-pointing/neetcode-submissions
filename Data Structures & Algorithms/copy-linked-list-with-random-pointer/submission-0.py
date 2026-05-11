"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        new_map = {None: None}
        curr = head
        while curr:
            copy = Node(curr.val)
            new_map[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = new_map[curr]
            copy.next = new_map[curr.next]
            copy.random = new_map[curr.random]
            curr = curr.next
        return new_map[head]