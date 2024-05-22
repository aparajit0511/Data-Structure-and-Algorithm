# Time Complexity - O(N)
# Space complexity - O(N) 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        from collections import deque
        queue = deque()
        queue.append((root,-inf))
        count_good_nodes = 0

        while queue:

            for _ in range(len(queue)):

                item, max_value = queue.popleft()

                if item.val >= max_value:
                    count_good_nodes += 1

                if item.left:

                    queue.append((item.left,max(item.val,max_value)))

                if item.right:

                    queue.append((item.right,max(item.val,max_value)))

        return count_good_nodes