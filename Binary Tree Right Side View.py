#Time complexity - O(N)
#Space Complexity - O(N+H)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if root is None:
            return []
        
        height = self.checkHeight(root)

        result = []
        print(height)

        for i in range(1,height+1):
            nodes = []
            nodes = self.levelOrderTraversal(root,i,nodes)
            print(nodes)
            result.append(nodes[-1])

        return result

    def checkHeight(self,root):
        if root is None:
            return 0
        else:
            left_height = 0
            right_height = 0

            left_height = self.checkHeight(root.left)
            right_height = self.checkHeight(root.right)

            return max(left_height,right_height) + 1

    def levelOrderTraversal(self,root,level,nodes):
        if root is None:
            return nodes
        elif level == 1:
            nodes.append(root.val)
            return nodes
        else:
            nodes = self.levelOrderTraversal(root.left,level-1,nodes)
            nodes = self.levelOrderTraversal(root.right,level-1,nodes)

            return nodes


#Time complexity - O(N)
#Space Complexity - O(N)
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque

        if root is None:
            return []

        queue = deque()
        queue.append(root)
        result = []

        while queue:
            level = []

            for _ in range(len(queue)):
                item = queue.popleft()
                if item.left != None:
                    queue.append(item.left)

                if item.right != None:
                    queue.append(item.right)

                level.append(item.val)

            result.append(level[-1])

        return result


