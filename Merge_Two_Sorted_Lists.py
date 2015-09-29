# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        dummy_node = ListNode(None)
        dummy_node.next = l1
        l1_node = dummy_node
        l2_node = l2
        while l1_node and l2_node:
            next_node = l1_node.next
            if not next_node:
                next_node.next = l2_node
                break
            if l2_node.val < next_node.val:
                copy_node = l2_node.next
                l1_node.next = l2_node
                l2_node.next = next_node
                l2_node = copy_node
            else:
                l1_node = l1_node.next
        return dummy_node.next
