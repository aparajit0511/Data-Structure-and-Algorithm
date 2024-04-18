# Time and Space Complexity - O(N) 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        result = []

        from collections import deque

        queue = deque()

        queue.append(root)

        while queue:
            level = []

            for _ in range(len(queue)):
                item = queue.popleft()
                level.append(item.val)

                if item.left != None:
                    queue.append(item.left)

                if item.right != None:
                    queue.append(item.right)
                
                print(len(queue))

            print("hi")

            result.append(level)

        return result


# Time O(N^2) and Space Complexity - O(N) 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []

        _height = self.height(root)
        result = []

        for i in range(1,_height+1):
            nodes = []
            nodes = self.checkNodes(root,nodes,i)
            result.append(nodes)

        return result

    def checkNodes(self,root,nodes,level):
        if root is None:
            return nodes
        elif level == 1:
            nodes.append(root.val)
        else:
            nodes = self.checkNodes(root.left,nodes,level-1)
            nodes = self.checkNodes(root.right,nodes,level-1)

        return nodes

    def height(self,root):

        if root is None:
            return 0

        else:
            left_height = 0
            right_height = 0

            if root.left:
                left_height = self.height(root.left)

            if root.right:
                right_height = self.height(root.right)

        return max(left_height,right_height) + 1


