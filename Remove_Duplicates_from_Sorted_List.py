# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        one_node = head
        while 1:
            if not one_node:
                break
            next_node = one_node.next
            if not next_node:
                break
            if next_node.val == one_node.val:
                one_node.next = next_node.next
            one_node = one_node.next
        return head
