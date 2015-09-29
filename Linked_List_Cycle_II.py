# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if not head or not head.next:
            return None
        fast, slow = head, head
        while 1:
            fast, slow = fast.next.next, slow.next
            if fast == slow:
                slow = head
                while slow != fast:
                    slow, fast = slow.next, fast.next
                return slow

            if not fast or not fast.next:
                return None
