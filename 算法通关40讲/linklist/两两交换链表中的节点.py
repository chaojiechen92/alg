# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while head and head.next:
            twonext = head.next.next
            prev.next = head.next
            head.next.next = head
            head.next = twonext
            prev = head
            head = twonext
        return dummy.next


if __name__ == "__main__":
    ret = Solution().swapPairs(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
    while ret:
        print(ret.val)
        ret = ret.next
