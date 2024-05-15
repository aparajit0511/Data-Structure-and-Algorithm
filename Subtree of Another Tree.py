# Time Complexity - O(N*M)
# Space complexity - O(H) 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if root is None:
            return False
        
        if subRoot is None:
            return True
            
            
        if self.checkSubTree(root,subRoot):
            return True

        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

    def checkSubTree(self,root1,root2):

        if root1 is None and root2 is None:
            return  True

        elif root1 is None and root2 != None or root1 != None and root2 is None:
            return False

        elif root1 != None and root2 != None:

            if root1.val != root2.val:
                return False
            else:
                return self.checkSubTree(root1.left,root2.left) and self.checkSubTree(root1.right,root2.right)



# Time Complexity - O(N*M)
# Space complexity - O(N) 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if root is None:
            return False

        if subRoot is None:
            return True

        stack = []
        stack.append(root)

        while stack:

            node = stack.pop()

            if node.val == subRoot.val and self.isSameTree(node,subRoot):
                return True

            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

        return False


    def isSameTree(self,root,subRoot):

        if root is None and subRoot is None:
            return True

        if not root or not subRoot:
            return False

        return root.val == subRoot.val and self.isSameTree(root.left,subRoot.left) and self.isSameTree(root.right,subRoot.right)
        