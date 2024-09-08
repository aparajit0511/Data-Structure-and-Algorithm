# Time Complexity - O(N)
# Space complexity - O(N) 

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
        
        # from collections import defaultdict

        if not head:
            return None

        hash_table = {}

        ptr = head

        while ptr:

            hash_table[ptr] = Node(ptr.val)
            ptr = ptr.next

        print(hash_table)

        ptr = head

        while ptr:
            hash_table[ptr].next = hash_table.get(ptr.next)
            hash_table[ptr].random = hash_table.get(ptr.random)
            ptr = ptr.next

        return hash_table[head]
