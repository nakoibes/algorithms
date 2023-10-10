# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return
        elements = list()
        node = head
        while node != None:
            elements.append(node.val)
            node = node.next

        root = ListNode(elements[-1])
        node = root
        for item in elements[-2::-1]:
            node.next = ListNode(item)
            node = node.next
        return root


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """MUTATING"""
        if head is None:
            return
        current_node = head
        previous_node = None
        while current_node is not None:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node

        return previous_node


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return
        if head.next is None:
            return head

        def rotate(previous_node: ListNode, node: ListNode):
            if node.next is not None:
                new_head = rotate(node, node.next)
            else:
                node.next = previous_node
                return node
            node.next = previous_node
            return new_head

        new_head = rotate(head, head.next)
        head.next = None

        return new_head


if __name__ == '__main__':
    s = Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    print(s.reverseList(node1))
