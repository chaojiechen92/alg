# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    # 自底向上的算法　从叶子节点算起
    # 还有自顶向下，取出高度对比
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return 0
        left = self.isBalanced(root.left)
        if left == -1:
            return -1
        right = self.isBalanced(root.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return max(left, right) + 1


if __name__ == "__main__":
    pass
