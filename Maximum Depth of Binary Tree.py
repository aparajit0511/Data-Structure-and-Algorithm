# Time Complexity - O(N)
# Space complexity - O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        return self.findDepth(root,0)

    def findDepth(self,root,max_Depth):

        if root is None:
            return max_Depth
        else:
            left_height = 0
            right_height = 0

            left_height = self.findDepth(root.left,max_Depth)
            right_height = self.findDepth(root.right,max_Depth)

            return max(max_Depth,left_height,right_height)+1


# Time Complexity - O(N)
# Space complexity - O(N)

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        from collections import deque

        queue = deque()
        queue.append((root,1))
        max_Depth = 0

        while queue:

            for _ in range(len(queue)):

                item , depth = queue.popleft()

                if item.left:
                    queue.append((item.left,depth+1))

                if item.right:
                    queue.append((item.right,depth+1))

                max_Depth = max(max_Depth,depth)
                

        return max_Depth

