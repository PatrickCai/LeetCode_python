# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy_node = ListNode(None)
        dummy_node.next = head
        slow_node = dummy_node
        fast_node = head
        for i in xrange(n):
            fast_node = fast_node.next
        if not fast_node:
            slow_node.next = slow_node.next.next
            return dummy_node.next
        while 1:
            fast_node = fast_node.next
            slow_node = slow_node.next
            if not fast_node:
                slow_node.next = slow_node.next.next
                break
        return dummy_node.next
