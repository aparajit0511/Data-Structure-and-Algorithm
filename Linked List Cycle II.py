# Time Complexity - O(N)
#Space complexity - O(N)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        set_ = set()
        ptr = head

        while ptr:
            if ptr in set_:
                return ptr

            set_.add(ptr)
            ptr = ptr.next

        return None

# Time Complexity - O(N)
#Space complexity - O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:

            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                break

        else:
            return None

        while head != slow:
            slow = slow.next
            head = head.next

        return head
