# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        ptr = head
        count_elements = 0

        while ptr:
            count_elements += 1
            ptr = ptr.next

        ptr = head
        head2 = None
        count_nodes = 0
        while ptr:
            if count_elements % 2 == 0 and count_nodes == (count_elements // 2)-1:
                head2 = ptr.next
                ptr.next = None
                break
            elif count_elements % 2 == 1 and count_nodes == (count_elements // 2):
                head2 = ptr.next
                ptr.next = None
                break

            ptr = ptr.next
            count_nodes +=1

        head2 = self.reverseLL(head2)

        ptr1 , ptr2 = head , head2
        temp1 , temp2 = None, None

        while ptr1 and ptr2:

            temp1 = ptr1.next
            temp2 = ptr2.next
            ptr1.next = ptr2
            ptr2.next = temp1
            ptr1 = temp1
            ptr2 = temp2


    def reverseLL(self,head):

        ptr = new = None
        current = head

        while current:
            ptr = current
            current = current.next
            ptr.next = new
            new = ptr

        head = new
        return head