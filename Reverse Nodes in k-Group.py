# Time complexity - O(N*k)
# Space complexity - O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        start = end = head
        count_elements = 0
        end_ptr = None
        head = None

        while end:

            count_elements += 1

            if count_elements % k == 0:

                end_ptr = end.next
                start, end = self.reverseLL(start,end)

                if head is None:
                    head = start
                    temp = end
                else:
                    temp.next = start
                    temp = end


                end.next = end_ptr
                start = end = end_ptr
            else:
                end = end.next

        return head

    def reverseLL(self,head,tail):
        tail.next = None
        current = ptr = head
        new = None
        temp = head

        while current != None:
            ptr = current
            current = current.next
            ptr.next = new
            new = ptr

        head = new
        tail = temp
        return head,tail
