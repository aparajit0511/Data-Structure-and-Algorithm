# Time Complexity - O(N)
# Space complexity - O(N)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        ptr = head
        array = []

        while ptr:
            array.append(ptr.val)
            ptr = ptr.next

        array.pop(len(array)//2)

        ptr = head = None

        for i in range(len(array)):
            if head is None:
                head = ListNode(array[i])
                ptr = head
            else:
                ptr.next = ListNode(array[i])
                ptr = ptr.next

        return head


# Time Complexity - O(N)
# Space complexity - O(1)     

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow = fast = head

        while fast != None and fast.next != None:

            fast = fast.next.next
            slow = slow.next

        ptr = head

        if ptr.next:
            while ptr.next != slow:
                print(ptr.val)
                ptr = ptr.next

            print(ptr.val,slow.val)
            ptr.next = slow.next
        else:
            return None

        return head
