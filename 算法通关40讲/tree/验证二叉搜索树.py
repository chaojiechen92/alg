# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 解法1 利用中序遍历　=> array 升序　
    def isValidBst1(self, root):
        """
                :type root: TreeNode
                :rtype: bool
                """
        self.ret = True
        self.prev = None

        def helper(root):
            if not root:
                return
            if self.ret:
                helper(root.left)
            if self.prev and self.prev.val > root.val:
                self.ret = False
            self.prev = root
            if self.ret:
                helper(root.right)
            return

        return self.ret

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        def valid(node, s, e):
            if not node:
                return True
            if node.val <= s and node.val >= e:
                return False

            return valid(node.left, s, node.val) and valid(node.right, node.val, e)

        return valid(root.left, float('inf'), root.val) and valid(root.right, root.val, float('inf'))


if __name__ == "__main__":
    pass
