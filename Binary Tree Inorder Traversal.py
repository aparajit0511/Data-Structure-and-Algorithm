# Time complexity - O(N)
# Space complexity - O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []

        return self.findInorder(root,result)

    def findInorder(self,root,result):

        if root is None:
            return result
        else:
            result = self.findInorder(root.left,result)
            result.append(root.val)
            result = self.findInorder(root.right,result)

            return result


# Time complexity - O(N)
# Space complexity - O(N)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        stack = []
        result = []
        current = root

        while True:

            if len(stack) == 0 and current is None:
                break

            while current != None:
                stack.append(current)
                current = current.left

            current = stack.pop()
            result.append(current.val)

            current = current.right

        return result