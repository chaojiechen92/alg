class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    # 快排还在超时
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def sort(snode, enode):
            if not snode or id(snode.next) == id(enode) or id(snode) == id(enode):
                return snode

            def partition(snode, enode):
                dummy = ListNode(0)
                dummy.next = snode
                node = snode.next
                snode.next = enode

                while id(node) != id(enode):
                    next = node.next
                    if node.val < snode.val:
                        node.next = dummy.next
                        dummy.next = node
                    else:
                        node.next = snode.next
                        snode.next = node
                    node = next

                return dummy.next, snode

            snode, midnode = partition(snode, enode)
            snode = sort(snode, midnode)
            enode = sort(midnode.next, enode)
            midnode.next = enode
            return snode

        return sort(head, None)

    # 用归并排序
    def sortList2(self, head):
        """
               :type head: ListNode
               :rtype: ListNode
               """
        if not head or not head.next:
            return head

        fast, slow = head, head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        s1 = self.sortList2(head)
        s2 = self.sortList2(slow)

        def merge(s1, s2):
            dummy = ListNode(0)
            prev = dummy
            while s1 and s2:
                if s1.val < s2.val:
                    prev.next = s1
                    prev = s1
                    s1 = s1.next
                else:
                    prev.next = s2
                    prev = s2
                    s2 = s2.next

            while s1:
                prev.next = s1
                prev = s1
                s1 = s1.next

            while s2:
                prev.next = s2
                prev = s2
                s2 = s2.next

            return dummy.next

        return merge(s1, s2)


if __name__ == "__main__":
    head = ListNode(3, ListNode(1, ListNode(2, ListNode(4))))
    ret = Solution().sortList2(head)
    while ret:
        print(ret.val)
        ret = ret.next
