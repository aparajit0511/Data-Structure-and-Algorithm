# Time Complexity - O(N)
# Space complexity - O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        from collections import deque
        queue = deque()
        queue.append(root)

        parent = {root.val:None}

        while p not in parent or q not in parent:

            item = queue.popleft()

            if item.left:
                queue.append(item.left)
                parent[item.left.val] = [item.val]

            if item.right:
                queue.append(item.right)
                parent[item.right.val] = [item.val]



        ancestor = set()

        while p:
            ancestor.add(p)
            p = parent[p]

        while q not in ancestor:
            q = parent[q]

        return q
