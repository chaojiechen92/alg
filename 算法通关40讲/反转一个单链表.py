# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev, node = None, head
        while node:
            next = node.next
            node.next = prev
            prev = node
            node = next
        return prev

    def reverseList2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        self.rets = None
        if not head:
            return self.rets

        def reverse(head ):
            if not head.next:
                self.rets = head
                return head
            prev = reverse(head.next)
            prev.next = head
            return head

        reverse(head)
        head.next = None
        return self.rets


if __name__ == "__main__":
    ret = Solution().reverseList2(ListNode(1, ListNode(2, ListNode(3))))
    while ret:
        print(ret.val)
        ret = ret.next
