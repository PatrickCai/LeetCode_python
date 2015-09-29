# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, node):
        self.val = x
        self.next = node

    def show(self):
        print("The self value is %s next value is %s" % (self.val, self.next.val))


class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if not head or not head.next or not head.next.next:
            return
        c = head.next
        n = c.next
        n_n = n.next if n else None
        c.next = None
        while 1:
            n.next = c
            if not n_n:
                head.next = n
                break
            else:
                c, n, n_n = n, n_n, n_n.next


# L4 = ListNode(4, None)
# L3 = ListNode(3, L4)
# L2 = ListNode(2, None)
L1 = ListNode(1, None)
head = ListNode(0, L1)

a = Solution()
a.reorderList(head)
print(head.show())
