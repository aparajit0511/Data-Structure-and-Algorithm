# Time Complexity - O(NlogN)
# Space complexity - O(N)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        result_array = []

        for i in lists:
            head = i
            while head:
                result_array.append(head.val)
                head = head.next

        result_array.sort()

        ptr = head = None

        for i in range(len(result_array)):

            if head is None:
                head = ListNode(result_array[i])
                ptr = head
            else:
                ptr.next = ListNode(result_array[i])
                ptr = ptr.next

        return head

