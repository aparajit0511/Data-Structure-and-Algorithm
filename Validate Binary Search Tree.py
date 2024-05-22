# Time Complexity - O(N)
# Space complexity - O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        inorder = []

        inorder = self.getInorder(root,inorder)

        for i in range(len(inorder)-1):
            if inorder[i] >= inorder[i+1]:
                return False

        return True


    def getInorder(self,root,inorder):
        if root is None:
            return inorder
        else:
            inorder = self.getInorder(root.left,inorder)
            inorder.append(root.val)
            inorder = self.getInorder(root.right,inorder)

            return inorder


# Time Complexity - O(N)
# Space complexity - O(N)

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        stack = []
        inorder = []
        current = root

        while True:

            if len(stack) == 0 and current is None:
                break

            while current != None:
                stack.append(current)
                current = current.left

            current = stack.pop()
            inorder.append(current.val)

            current = current.right


        for i in range(len(inorder)-1):
            if inorder[i] >= inorder[i+1]:
                return False

        return True