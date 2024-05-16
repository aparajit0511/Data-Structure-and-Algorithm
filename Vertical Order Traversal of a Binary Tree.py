# Time Complexity - O(N) + O(NlogN)
# Space complexity - O(N) 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        from collections import deque
        result = []

        deque = deque()

        deque.append((root,0))

        hash_table = {0:[root.val]}

        while deque:

            for _ in range(len(deque)):

                item , depth = deque.popleft()

                if item.left:
                    if depth - 1 not in hash_table:
                        hash_table[depth-1] = [item.left.val]
                    else:
                        hash_table[depth-1].append(item.left.val)

                    deque.append((item.left,depth-1))

                if item.right:
                    if depth + 1 not in hash_table:
                        hash_table[depth+1] = [item.right.val]
                    else:
                        hash_table[depth+1].append(item.right.val)

                    deque.append((item.right,depth+1))


        hash_table = dict(sorted(hash_table.items(),key = lambda x:x[0]))


        for key,value in hash_table.items():
            if len(value) > 1:
                value.sort()

            result.append(value)

        return result


# Time Complexity - O(N*N)
# Space complexity - O(H) 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        hash_table = {}

        height_ = self.findheight(root)
        depth = 0

        for i in range(1,height_+1):
            
            hash_table = self.findLevelOrder(root,i,depth,hash_table)



        hash_table = dict(sorted(hash_table.items(),key = lambda x:x[0]))
        result = []

        for key,value in hash_table.items():
            if len(value) > 1:
                value.sort()

            result.append(value)

        return result


    def findheight(self,root):

        if root is None:
            return 0
        else:
            left_height = 0
            right_height = 0

            left_height = self.findheight(root.left)
            right_height = self.findheight(root.right)

            return max(left_height,right_height)+1


    def findLevelOrder(self,root,level,depth,hash_table):

        if root is None:
            return hash_table
        elif level == 1:
            if depth not in hash_table:
                hash_table[depth] = [root.val]
            else:
                hash_table[depth].append(root.val)
            return hash_table
        else:
            hash_table = self.findLevelOrder(root.left,level-1,depth-1,hash_table)
            hash_table = self.findLevelOrder(root.right,level-1,depth+1,hash_table)

            return hash_table



# Time Complexity - O(N) + O(NlogN)
# Space complexity - O(N) 


# Leetcode problem solution

from collections import defaultdict, deque

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        # Create a defaultdict to store nodes at each column
        column_table = defaultdict(list)

        # Use a deque for BFS traversal, each item includes node and its position
        queue = deque([(root, 0)])  # Start with root at position (0, 0)

        # Perform BFS traversal
        while queue:
            # Record nodes at the current level (same column)
            level_nodes = defaultdict(list)

            for _ in range(len(queue)):
                node, column = queue.popleft()
                level_nodes[column].append(node.val)  # Store node value at its column
                if node.left:
                    queue.append((node.left, column - 1))  # Move to the left, decrease column by 1
                if node.right:
                    queue.append((node.right, column + 1))  # Move to the right, increase column by 1

            # Merge the level_nodes into column_table
            for col, nodes in level_nodes.items():
                column_table[col].extend(sorted(nodes))  # Sort nodes by their values in the same column

        # Sort the column_table by keys (column positions)
        sorted_columns = sorted(column_table.items(), key=lambda x: x[0])

        # Extract the values (nodes) from the sorted_columns
        vertical_order = [nodes for col, nodes in sorted_columns]

        return vertical_order
