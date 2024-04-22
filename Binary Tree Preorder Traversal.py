# Time complexity - O(N)
# Space complexity - O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []

        return self.findPreorder(root,result)

    def findPreorder(self,root,result):

        if root is None:
            return result
        else:
            result.append(root.val)
            result = self.findPreorder(root.left,result)
            result = self.findPreorder(root.right,result)

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
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if root is None:
            return []
        
        result = []
        stack = []

        stack.append(root)

        while stack:

            current = stack.pop()
            result.append(current.val)

            if current.right != None:
                stack.append(current.right)

            if current.left != None:
                stack.append(current.left)

        return result

