# Time Complexity - O(N)
# Space complexity - O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        inorder = []
        
        inorder = self.findInorder(root,inorder)

        return inorder[k-1]


    def findInorder(self,root,inorder):

        stack = []
        current = root

        while True:

            if current is None and len(stack) == 0:
                break

            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            inorder.append(current.val)

            current = current.right

        return inorder


# Time Complexity - O(N)
# Space complexity - O(1)

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = [0]  # Use a list to allow the counter to be updated within the helper function
        answer = self.findInorder(root, counter, k)
        return answer.val if answer else None

    def findInorder(self, root: Optional[TreeNode], counter: list, k: int) -> Optional[TreeNode]:
        if root is None:
            return None
        
        # Search in the left subtree
        left = self.findInorder(root.left, counter, k)
        if left:
            return left
        
        # Increment the counter and check if the current node is the kth smallest
        counter[0] += 1
        if counter[0] == k:
            return root
        
        # Search in the right subtree
        return self.findInorder(root.right, counter, k)
        
