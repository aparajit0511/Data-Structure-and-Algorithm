# Time Complexity - O(N)
# Space complexity - O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        
        from collections import deque

        queue = deque()
        result = []
        queue.append(root)
        count = 0

        while queue:
            count += 1
            levels = []

            for _ in range(len(queue)):

                item = queue.popleft()

                if item.left:
                    queue.append(item.left)

                if item.right:
                    queue.append(item.right)

                levels.append(item.val)

            if count % 2 == 0:
                levels.reverse()

            result.append(levels)

        return result


# Time Complexity - O(N*2)
# Space complexity - O(H)

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        height = self.findHeight(root)

        result = []

        for i in range(1,height+1):
            nodes = []
            nodes = self.findZigZag(root,i,nodes)

            if i % 2 == 0:
                nodes.reverse()

            result.append(nodes)

        return result


    def findHeight(self,root):

        if root is None:
            return 0
        else:
            left_height = 0
            right_height = 0

            left_height = self.findHeight(root.left)
            right_height = self.findHeight(root.right)

            return max(left_height,right_height)+1


    def findZigZag(self,root,level,nodes):

        if root is None:
            return nodes
        elif level == 1:
            nodes.append(root.val)
            return nodes
        else:

            nodes = self.findZigZag(root.left,level-1,nodes)
            nodes = self.findZigZag(root.right,level-1,nodes)

            return nodes