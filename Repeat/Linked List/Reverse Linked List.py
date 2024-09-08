# Time Complexity - O(N)
# Space complexity - O(1) 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        current = head
        ptr = new = None

        while current != None:
            ptr = current
            current = current.next
            ptr.next = new
            new = ptr

        head= new

        return head
        

# Time Complexity - O(N)
# Space complexity - O(N) 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        ptr = new = None
        
        return self.recursion(current,ptr,new)


    def recursion(self,current,ptr,new):

        if current is None:
            return new

        ptr = current
        current = current.next
        ptr.next = new
        new = ptr
        new = self.recursion(current,ptr,new)

        return new