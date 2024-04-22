# Time complexity - O(N)
# Space complexity - O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if root is None:
            return []

        stack = deque()
        result = []

        current = root

        while current or stack:

            if current:
                result.append(current.val)
                stack.append(current)
                current = current.right
            else:
                current = stack.pop()
                current = current.left
        
        result.reverse()

        return result


# Time complexity - O(N)
# Space complexity - O(N)

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []

        return self.findPostorder(root,result)

    def findPostorder(self,root,result):

        if root is None:
            return result
        else:

            result = self.findPostorder(root.left,result)
            result = self.findPostorder(root.right,result)

            result.append(root.val)

            return result