class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


class BinarySearchTree():
    def __init__(self):
        self.root = TreeNode(0)

    def find(self, val):
        node = self.root
        while node and node.val != val:
            if node.val > val:
                node = node.left
            else:
                node = node.right

        return node

    def insert(self, val):
        if not val:
            return

        node = self.root
        prev = None
        while node and node.val != val:
            if node.val > val:
                prev = node
                node = node.left
            else:
                prev = node
                node = node.right

        if node:
            return
        new_node = TreeNode(val)
        if prev.val < val:
            prev.right = new_node
        if prev.val > val:
            prev.left = new_node
        return

    def delete(self, val):
        node = self.root
        prev = None
        while node and node.val != val:
            if node.val > val:
                prev = node
                node = node.left
            else:
                prev = node
                node = node.right

        if not node:
            return
        if node.left and node.right:
            node2 = node.right
            prev2 = node
            while node2.next:
                prev2 = node2
                node2 = node2.left
            node.val = node2.val
            prev = prev2
            node = node2

        if prev.right == node:
            prev.right = node.left if node.left else node.right
        else:
            prev.left = node.left if node.left else node.right
        return

    def test(self):
        self.root.left = TreeNode(-1)
        self.root.right = TreeNode(2)


if __name__ == "__main__":
    btree = BinarySearchTree()
    btree.insert(3)
    btree.insert(2)
    btree.insert(1)
    btree.delete(2)
    print(btree.find(2))
