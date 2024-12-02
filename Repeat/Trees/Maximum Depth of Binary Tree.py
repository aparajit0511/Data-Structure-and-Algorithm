# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        from collections import deque
        queue = deque()

        queue.append((root,0))

        while queue:

            item,depth = queue.popleft()

            if item.left:
                queue.append((item.left,depth+1))

            if item.right:
                queue.append((item.right,depth+1))

        return depth+1




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0

        def findHeight(root,height):
            if root is None:
                return 0
            else:
                left_height = 0
                right_height = 0

                left_height = findHeight(root.left,left_height+1)
                right_height = findHeight(root.right,right_height+1)

                if left_height > right_height:
                    return left_height+1
                else:
                    return right_height+1

        return findHeight(root,0)