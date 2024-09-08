# Time Complexity - O(M+NLog(M+N))
# Space complexity - O(M+N)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = list1
        arr_list = []

        while head:
            arr_list.append(head.val)
            head = head.next

        head = list2

        while head:
            arr_list.append(head.val)
            head = head.next

        arr_list.sort()

        head = ptr = None

        for num in arr_list:

            if head is None:
                head = ListNode(num)
                ptr = head
            else:
                ptr.next = ListNode(num)
                ptr = ptr.next

        return head


# Time Complexity - O(M+N)
# Space complexity - O(M+N)

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head1 =  ptr1 = list1
        head2 = ptr2 = list2
        head3 = ptr3 = None

        if not head1 and head2:
            return head2
        elif not head2 and head1:
            return head1
        # print("hiiiii")

        def createLL(val,head,ptr):
            if head is None:
                head = ListNode(val)
                ptr = head
            else:
                ptr.next = ListNode(val)
                ptr = ptr.next

            return head,ptr

        while ptr1 and ptr2:

            if ptr1.val <= ptr2.val:
                head3,ptr3 = createLL(ptr1.val,head3,ptr3)
                ptr1 = ptr1.next
                # print("hi",head3,ptr3)
            elif ptr2.val < ptr1.val:
                head3,ptr3  = createLL(ptr2.val,head3,ptr3)
                ptr2 = ptr2.next
                # print("hi2")

        if ptr1:
            ptr3.next = ptr1
        elif ptr2:
            ptr3.next = ptr2

        return head3