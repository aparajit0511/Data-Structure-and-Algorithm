# Time Complexity - O(N)
# Space complexity - O(N)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        odd_array = []
        even_array = []


        count_elements = 1

        ptr = head

        while ptr:
            if count_elements % 2 == 1:
                odd_array.append(ptr.val)
            else:
                even_array.append(ptr.val)

            count_elements += 1
            ptr = ptr.next

        odd_array.extend(even_array)

        ptr = head = None

        for i in range(len(odd_array)):
            if head is None:
                head = ListNode(odd_array[i])
                ptr = head
            else:
                ptr.next = ListNode(odd_array[i])
                ptr = ptr.next

        return head


# Time Complexity - O(N)
# Space complexity - O(1)

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return None
        
        odd_ptr = head
        even_ptr = evenptr_head =  None
        count_elements = 1


        while odd_ptr and odd_ptr.next:

            if count_elements % 2 == 1:
                if evenptr_head is None:
                    evenptr_head = odd_ptr.next
                    even_ptr = evenptr_head
                    odd_ptr.next = even_ptr.next

                else:
                    even_ptr.next = odd_ptr.next
                    even_ptr = even_ptr.next
                    odd_ptr.next = even_ptr.next

                
                even_ptr.next = None
                if odd_ptr.next != None:
                    odd_ptr = odd_ptr.next
                count_elements += 2


        odd_ptr.next = evenptr_head

        return head