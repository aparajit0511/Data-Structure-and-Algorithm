# Time Complexity - O(N)
# Space complexity - O(H) 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if root.left is None and root.right is None:
            return True

        return self.checkMirror(root.left,root.right)

    def checkMirror(self,root1,root2):

        if root1 is None and root2 is None:
            return True

        elif (root1 is None and root2 != None) or (root1 != None and root2 is None):
            return False
        elif root1 != None and root2 != None:

            if root1.val != root2.val:
                return False
            else:
                return self.checkMirror(root1.left,root2.right) and self.checkMirror(root1.right,root2.left)


# Time Complexity - O(N)
# Space complexity - O(N)

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        if root.left is None and root.right is None:
            return True

        from collections import deque

        queue1 = deque()
        queue2 = deque()

        queue1.append(root.left)
        queue2.append(root.right)

        while queue1 and queue2:

            if len(queue1) != len(queue2):
                return False

            else:

                for _ in range(len(queue1)):

                    item1 = queue1.popleft()
                    item2 = queue2.popleft()

                    if item1 and item2 and item1.val != item2.val or (item1 is None and item2 != None) or (item1 != None and item2 is None):
                        return False

                    if item1:
                        queue1.append(item1.right)
                        queue1.append(item1.left)

                    if item2:
                        queue2.append(item2.left)
                        queue2.append(item2.right)

        return True
