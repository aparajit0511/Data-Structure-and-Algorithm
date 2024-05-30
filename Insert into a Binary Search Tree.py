# Time Complexity - O(N)
# Space complexity - O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if root is None:
            root = TreeNode(val)
            return root
        elif  val <= root.val:
            root.left = self.insertIntoBST(root.left,val)
        else:
            root.right = self.insertIntoBST(root.right,val)

        return root


# Time Complexity - O(N)
# Space complexity - O(N)

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if root is None:
            root = TreeNode(val)
            return root

        current = root
        parent = None

        while current:
            if val <= current.val:
                parent = current
                current = current.left
            else:
                parent = current
                current = current.right

        if val <= parent.val:
            parent.left = TreeNode(val)
        else:
            parent.right = TreeNode(val)

        return root
