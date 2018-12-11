# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        s = set()
        node = head
        while node:
            if id(node) in s:
                return node
            s.add(id(node))
            node = node.next
        return None


if __name__ == "__main__":
    pass
