# Time complexity - O(N+k)
# Space complexity - O(N)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        from collections import deque

        if head is None:
            return None

        queue = deque()

        ptr = head

        while ptr:
            queue.append(ptr.val)
            ptr = ptr.next

        while k > 0:
            item = queue.pop()
            queue.appendleft(item)
            k = k-1

        ptr = head = None

        for i in range(len(queue)):

            if head is None:
                head = ListNode(queue[i])
                ptr = head
            else:
                ptr.next = ListNode(queue[i])
                ptr = ptr.next

        return head


# Time complexity - O(N)
# Space complexity - O(1)
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if head is None or k  == 0 or head.next is None:
            return head
        
        slow = fast = ptr = head
        count = 0

        while ptr:
            count += 1
            ptr = ptr.next
        k = k % count

        for _ in range(k):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        temp = slow.next
        fast.next = head
        slow.next = None

        return temp if k != 0 else head