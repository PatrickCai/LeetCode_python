# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def rotateRight(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        current_n = dummy
        index = 0
        while index < k:
            current_n = current_n.next
            if not current_n:
                current_n = dummy.next
            index += 1
        return_node = current_n.next if current_n else head

        index_n = dummy
        while index_n.next:
            index_n = index_n.next
        index_n.next = current_n
        current_n.next = None
        return return_node
