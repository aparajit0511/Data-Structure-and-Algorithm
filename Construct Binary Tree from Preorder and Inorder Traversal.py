# Time Complexity - O(N)
# Space complexity - O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if len(preorder) == 0 or len(inorder) == 0:
            return None

        stack = []
        root = TreeNode(preorder[0])
        stack.append(root)
        pre = 1
        ino = 0

        while pre < len(preorder):
            current = TreeNode(preorder[pre])
            pre += 1

            previous = None
            while stack and stack[-1].val == inorder[ino]:
                previous = stack.pop()
                ino += 1

            if previous:
                previous.right = current
            else:
                stack[-1].left = current

            stack.append(current)

        return root
