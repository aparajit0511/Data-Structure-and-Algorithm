# Time Complexity - O(N)
# Space complexity - O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = [0]

        self.findLongestPath(root,max_diameter)

        return max_diameter[0]

    def findLongestPath(self,root,max_diameter):

        if not root:
            return 0

        left_height = self.findLongestPath(root.left,max_diameter)
        right_height = self.findLongestPath(root.right,max_diameter)

        max_diameter[0] = max(max_diameter[0],(left_height+right_height))

        return 1 + max(left_height,right_height)