# Time complexity - O(N)
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

        if not head:
            # head is none
            return None

        hash_table = {}

        ptr = head

        # Traverse the original list and for each node, create a corresponding new node.
        # Store the mapping in old_to_new.
        while ptr:
            hash_table[ptr] = Node(ptr.val)
            ptr = ptr.next

        ptr = head
        
        # For each node, set its corresponding new node's next and random pointers based on the hash map.
        while ptr:
            hash_table[ptr].next = hash_table.get(ptr.next)
            hash_table[ptr].random = hash_table.get(ptr.random)
            ptr = ptr.next

        return hash_table[head]
