# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:

        if not root1:
            return root2

        if not root2:
            return root1

        root = TreeNode(root1.val + root2.val)
        stack = [(root1, root2, root)]

        while stack:
            n1, n2, n = stack.pop()
            if n1.left and n2.left:
                n.left = TreeNode(n1.left.val + n2.left.val)
                stack.append((n1.left, n2.left, n.left))
            elif not n1.left:
                n.left = n2.left
            else:
                n.left = n1.left

            if n1.right and n2.right:
                n.right = TreeNode(n1.right.val + n2.right.val)
                stack.append((n1.right, n2.right, n.right))
            elif not n1.right:
                n.right = n2.right
            else:
                n.right = n1.right

        return root
