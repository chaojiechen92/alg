class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

    def __str__(self):
        return str(self.val)


class DoubleLink():
    def __init__(self):
        self.head = Node(0)
        self.total = 0

    def size(self):
        return self.total

    def isEmpty(self):
        return self.total == 0

    def getNode(self, i):
        if self.isEmpty():
            return -1
        if i >= self.size():
            return -1

        node = self.head.next
        j = 0
        while node and j < i:
            node = node.next
            j += 1
        return node

    def insert(self, i, val):
        if i < self.size():
            new_node = Node(val)
            j = 0
            node = self.head.next
            while j < i:
                node = node.next
                j += 1
            node.prev.next = new_node
            new_node.prev = node.prev
            node.prev = new_node
            new_node.next = node

            return True
        return False

    def delete(self, i):
        if i < self.size():
            node = self.head.next
            j = 0
            while j < i:
                node = node.next
                j += 1
            node.prev.next = node.next
            node.next.prev = node.prev
            return True
        return False


if __name__ == "__main__":
    pass
