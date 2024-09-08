# Time Complexity - O(N)
# Space complexity - O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        count_nodes = 0

        ptr = head

        while ptr:
            count_nodes += 1
            ptr = ptr.next

        if count_nodes == 1 and n == 1:
            return None

        slow = head

        diff = 1

        while diff < count_nodes - n:

            slow = slow.next
            diff += 1

        if  count_nodes - n == 0:
            head = slow.next
            return head
        
        slow.next = slow.next.next

        return head

