# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    # 广度优先算法
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        q = [root] if root else []
        while q:
            cur_len = len(q)
            i = 0
            level_vals = []
            while i < cur_len:
                node = q.pop(0)
                level_vals.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                i += 1
            ret.append(level_vals)

        return ret


if __name__ == "__main__":
    print(Solution().levelOrder(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))
