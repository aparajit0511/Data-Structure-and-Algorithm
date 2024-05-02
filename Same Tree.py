#Time complexity - O(N)
#Space Complexity - O(H)

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        return self.checkSameTree(p,q)

    def checkSameTree(self,root1,root2):

        if (root1 is None and root2 != None) or (root1 != None and root2 is None):
            return False

        elif root1 is None and root2 is None:
            return True

        elif root1 != None and root2 != None:

            if root1.val != root2.val:
                return False
            else:
                return self.checkSameTree(root1.left,root2.left) and self.checkSameTree(root1.right,root2.right)


#Time complexity - O(N)
#Space Complexity - O(N)
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        from collections import deque

        queue1 = deque()
        queue2 = deque()

        queue1.append(p)
        queue2.append(q)

        while queue1 and queue2:

            if len(queue1) != len(queue2):
                return False
            else:

                for _ in range(len(queue1)):

                    item1 = queue1.popleft()
                    item2 = queue2.popleft()

                    if item1 != None and item2 is None or item2 != None and item1 is None:
                        return False

                    if item1 and item2 and item1.val != item2.val:
                        return False

                    if item1:
                        queue1.append(item1.left)
                        queue1.append(item1.right)

                    if item2:
                        queue2.append(item2.left)
                        queue2.append(item2.right)

        return True