# Time Complexity - O(N)
# Space complexity - O(N) 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        slow = fast = head
        count_k = 0

        def reverseLL(head,tail):
            current = head
            ptr = new = None
            tail.next = None

            while current != None:
                if current is head:
                    tail = current

                ptr = current
                current = current.next
                ptr.next = new
                new = ptr

            head = new
            return head,tail

        found = True

        while fast != None:
            count_k += 1
            if count_k % k == 0:
                count_k = 0
                fast_next = fast.next
                if slow == head and found:
                    head_R,tail_R = reverseLL(slow,fast)
                    head = head_R
                    found = False
                else:
                    head_R,tail_R = reverseLL(slow.next,fast)
                    slow.next = head_R

                fast = tail_R
                slow = tail_R
                fast.next = fast_next
                

            fast = fast.next

        return head

