# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        or_node = RandomListNode(0)
        or_node.next = head
        dummy_node = RandomListNode(0)
        co_node = dummy_node
        or_dict = {}
        co_nodes = []
        while or_node.next:
            or_node = or_node.next
            co_node.next = RandomListNode(or_node.label)
            co_node = co_node.next
            or_dict[or_node.label] = or_node
            co_nodes.append(co_node)
        for node in co_nodes:
            random_node = or_dict[node.label].random
            if random_node:
                node.random = RandomListNode(random_node.label)
            else:
                node.random = None
        return dummy_node.next
