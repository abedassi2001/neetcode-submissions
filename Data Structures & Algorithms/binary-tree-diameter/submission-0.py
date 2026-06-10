# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0 

        def find_diameter(root):
            nonlocal diameter
            if root == None :
                return 0 

            left_depth = find_diameter(root.left)
            right_depth = find_diameter(root.right)

            depth = max(right_depth , left_depth ) + 1 

            diameter = max( left_depth + right_depth , diameter)

            return depth 

        find_diameter(root)

        return diameter 








        