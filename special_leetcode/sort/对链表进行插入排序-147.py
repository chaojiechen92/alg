# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        next = head.next
        head.next = None
        dummy = ListNode(0)
        dummy.next = head
        while next:
            cur = dummy.next
            prev = dummy
            while cur and cur.val < next.val:
                prev = cur
                cur = cur.next
            node = next.next
            next.next = prev.next
            prev.next = next
            next = node

        return dummy.next


if __name__ == "__main__":
    pass
