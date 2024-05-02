#Time complexity - O(N)
#Space Complexity - O(H)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if root is None:
            return True
        
        height = self.checkHeight(root)

        if height == -1:
            return False

        return True


    def checkHeight(self,root):

        if root is None:
            return 0
        else:
            left_height = 0
            right_height = 0

            if root.left:
                left_height = self.checkHeight(root.left)

            if root.right:
                right_height = self.checkHeight(root.right)

            if left_height == -1 or right_height == -1:
                return -1

            if abs(left_height - right_height) > 1:
                return -1
            elif left_height > right_height:
                return left_height + 1
            else:
                return right_height + 1



#Time complexity - O(N)
#Space Complexity - O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if root is None:
            return True

        stack = []
        stack.append((root,False))

        depth = {}

        while stack:

            node , visited = stack.pop()

            if node is None:
                continue

            if visited:
                left_depth = depth.get(node.left,0)
                right_depth = depth.get(node.right,0)

                if abs(left_depth - right_depth) > 1:
                    return False

                depth[node] = max(left_depth,right_depth)+1
            else:
                stack.append((node,True))
                stack.append((node.right,False))
                stack.append((node.left,False))


        return True