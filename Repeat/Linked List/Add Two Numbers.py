# Time Complexity - O(max(M,N))
# Space complexity - O(max(M,N)) 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        ptr1 = l1
        ptr2 = l2
        ptr3 = head = None
        carry = 0

        def createLL(head,ptr,val):
            if head is None:
                head = ListNode(val)
                ptr = head
            else:
                ptr.next = ListNode(val)
                ptr = ptr.next

            return head,ptr


        while ptr1 and ptr2 :

            sum = ptr1.val + ptr2.val + carry
            if sum > 9:
                carry = sum // 10
                sum = sum % 10
                head,ptr3 = createLL(head,ptr3,sum)
            else:
                carry = 0
                head,ptr3 = createLL(head,ptr3,sum)

            ptr1 = ptr1.next
            ptr2 = ptr2.next


        if ptr1 and carry == 0:
            ptr3.next = ptr1
            return head
        elif ptr1 and carry != 0:
            while ptr1:
                sum = ptr1.val + carry
                if sum > 9:
                    carry = sum // 10
                    sum = sum % 10
                    head,ptr3 = createLL(head,ptr3,sum)
                else:
                    carry = 0
                    head,ptr3 = createLL(head,ptr3,sum)

                ptr1 = ptr1.next


        if ptr2 and carry == 0:
            ptr3.next = ptr2
            return head
        elif ptr2 and carry != 0:
            while ptr2:
                sum = ptr2.val + carry
                if sum > 9:
                    carry = sum // 10
                    sum = sum % 10
                    head,ptr3 = createLL(head,ptr3,sum)
                else:
                    carry = 0
                    head,ptr3 = createLL(head,ptr3,sum)

                ptr2 = ptr2.next

        if carry != 0:
            head,ptr3 = createLL(head,ptr3,carry)

        return head
