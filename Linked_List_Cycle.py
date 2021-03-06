# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if not head:
            return False
        nodes = []
        nodes.append(head)
        c = head
        while c.next:
            if c.next in nodes:
                return True
            else:
                nodes.append(c.next)
                c = c.next
        return False
