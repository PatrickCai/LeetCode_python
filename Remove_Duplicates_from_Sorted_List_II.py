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
        dummy_node = ListNode(None)
        dummy_node.next = head
        pre_node = dummy_node
        one_node = dummy_node.next
        is_duplicate = False
        while pre_node and one_node:
            next_node = one_node.next
            if not next_node:
                if is_duplicate:
                    pre_node.next = None
                break
            if one_node.val == next_node.val:
                one_node.next = next_node.next
                is_duplicate = True
            else:
                if is_duplicate:
                    pre_node.next = next_node.next
                else:
                    pre_node = one_node
                    one_node = one_node.next
                    is_duplicate = False
        return dummy_node.next
