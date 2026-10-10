# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        prev=None
        while node and node.next:
            next_node=node.next
            node.val=next_node.val
            prev=node
            node=next_node
        else:
            prev.next=None