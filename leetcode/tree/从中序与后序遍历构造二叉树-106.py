# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not postorder:
            return None
        val = postorder.pop()
        for i, ival in enumerate(inorder):
            if ival == val:
                mid = i
                break
        root = TreeNode(val)
        root.left = self.buildTree(inorder[0:mid], postorder[0:mid])
        root.right = self.buildTree(inorder[mid + 1:], postorder[mid:])

        return root


if __name__ == "__main__":
    pass