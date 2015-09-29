# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy_node = ListNode(None)
        dummy_node.next = head
        pre_node = dummy_node
        par_node = head    
        while par_node:
            if par_node.val >= x:
                break
            else:
                pre_node = pre_node.next
                par_node = par_node.next
        next_node = par_node.next
        next_part = next_node.next
        while next_node:
            if next_node.val < x:
                pre_node.next = next_node
                next_node.next = par_node
                par_node.next = next_part

            next_node = next_part
            if not next_part:
                break
            else:
                next_part = next_part.next
        return dummy_node.next

