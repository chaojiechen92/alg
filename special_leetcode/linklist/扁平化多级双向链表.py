"""
# Definition for a Node.

"""


class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        dummy = Node(0, None, None, None)
        dummy.next = head
        prev = dummy
        s = []
        node = head
        while node or s:
            if node and node.child:
                s.append(node)
                prev = node
                node = node.child
            else:
                if not node:
                    val = s.pop()
                    prev.next = val.next
                    if val.next:
                        val.next.prev = prev
                    val.next = val.child
                    val.child.prev = val
                    val.child = None
                    node = prev

                prev = node
                node = node.next

        return dummy.next


if __name__ == "__main__":
    pass
