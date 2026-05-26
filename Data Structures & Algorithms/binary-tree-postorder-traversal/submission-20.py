# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        stack = []
        visit = []
        res = []
        cur = root

        while cur or stack:
            if cur:
                stack.append(cur)
                visit.append(False)
                cur = cur.left
            else:
                visited = visit.pop()
                cur = stack.pop()
                if visited:
                    res.append(cur.val)
                    cur = None
                else:
                    stack.append(cur)
                    visit.append(True)
                    cur = cur.right
        return res
