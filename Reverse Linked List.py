# Time complexity - O(N)
# Space complexity - O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current  = head
        new = ptr =  None

        while current != None:
            ptr = current
            current = current.next
            ptr.next = new
            new = ptr

        head = new

        return head

# Time complexity - O(N)
# Space complexity - O(N)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current = head
        new = ptr = None

        return self.returnReverse(current,new,ptr)

    def returnReverse(self,current,new,ptr):

        if current is None:
            return new
        else:
            ptr = current
            current = current.next
            ptr.next = new
            new = ptr

            return self.returnReverse(current,new,ptr)