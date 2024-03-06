# Time Complexity - O(N)
#Space complexity - O(N)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        array = []

        ptr = head

        while ptr:
            array.append(ptr.val)
            ptr = ptr.next

        count_middle = 0
        ptr = head

        while ptr:
            if count_middle == len(array)//2:
                return ptr
            ptr = ptr.next
            count_middle += 1

# Time Complexity - O(2N)
#Space complexity - O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        ptr = head
        count_nodes = 0

        while ptr:
            count_nodes += 1
            ptr = ptr.next

        count_middle = 0
        ptr = head

        while ptr:
            if count_middle == count_nodes//2:
                return ptr
            ptr = ptr.next
            count_middle += 1


# Time Complexity - O(N)
#Space complexity - O(1) 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

        slow = fast = head

        while fast and fast.next:

            fast = fast.next.next

            slow = slow.next

        return slow