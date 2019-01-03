class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    # O(2n) 空间复杂度n
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """

        dummy = RandomListNode(0)
        prev = dummy
        node = head
        d = {}
        while node:
            new_node = RandomListNode(node.label)
            d[id(node)] = new_node
            prev.next = new_node
            prev = new_node
            node = node.next

        node = head
        new_node = dummy.next
        while node:
            new_node.random = d[id(node.random)] if node.random else None
            node = node.next
            new_node = new_node.next
        return dummy.next

    def copyRandomList2(self, head):

        node = head
        while node:
            new_node = RandomListNode(node.label)
            next = node.next
            new_node.next = node.next
            node.next = new_node
            node = next

        node = head

        while node:
            node.next.random = node.random.next if node.random else None
            node = node.next.next

        node = head
        chead = node.next if node else None
        while node:
            next = node.next.next
            node.next.next = next.next if next else None
            node.next = next
            node = next

        return chead


if __name__ == "__main__":
    pass
