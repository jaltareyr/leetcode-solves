# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        count = [-1, 0]
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            if count[1] >= k:
                return
            count[0] = root.val
            count[1] += 1
            result.append(root.val)
            inorder(root.right)
        
        result = []
        inorder(root)
        return count[0]
        