# Time Complexity - O(N)
#Space complexity - O(N)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        result = []

        ptr = list1

        while ptr:
            result.append(ptr.val)
            ptr = ptr.next

        ptr = list2

        while ptr:
            result.append(ptr.val)
            ptr = ptr.next

        result.sort()
        ptr = head = None
        

        for i in range(len(result)):

            if head is None:
                head = ListNode(result[i])
                ptr = head
            else:
                ptr.next = ListNode(result[i])
                ptr = ptr.next

        return head

# Time Complexity - O(N)
#Space complexity - O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        

        ptr1 = list1
        ptr2 = list2
        ptr3 = head = None

        while ptr1 and ptr2:

            if ptr1.val < ptr2.val:
                if head is None:
                    head = ListNode(ptr1.val)
                    ptr3 = head
                else:
                    ptr3.next = ListNode(ptr1.val)
                    ptr3 = ptr3.next

                ptr1 = ptr1.next

            else:
                if head is None:
                    head = ListNode(ptr2.val)
                    ptr3 = head
                else:
                    ptr3.next = ListNode(ptr2.val)
                    ptr3 = ptr3.next

                ptr2 = ptr2.next

        if ptr1 is not None:
            if head is None:
                head = ptr1
            else:
                ptr3.next = ptr1
        elif ptr2 is not None:
            if head is None:
                head = ptr2
            else:
                ptr3.next = ptr2

        return head


