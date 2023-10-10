# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)+"|"+str(id(self))


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        elements = list()
        node = head
        while node != None:
            elements.append(node.val)
            node = node.next
        return elements == elements[::-1]


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        front_pointer = head

        def check_recursively(node: ListNode):
            if node.next:
                status = check_recursively(node.next)
            else:
                if node.val != front_pointer.val:
                    return False
                if front_pointer.next:
                    front_pointer.val = front_pointer.next.val
                    front_pointer.next = front_pointer.next.next
                return True

            if not status:
                return False

            if node.val != front_pointer.val:
                return False
            # if node == front_pointer.next or node.next == front_pointer.next:
            #     return True
            if front_pointer.next:
                front_pointer.val = front_pointer.next.val
                front_pointer.next = front_pointer.next.next

            return True

        return check_recursively(head)


class Solution:
    front_pointer = None

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # self.front_pointer = head
        self.front_pointer = head

        def check_recursively(node: ListNode):
            if node:
                if not check_recursively(node.next):
                    return False
                if node.val != self.front_pointer.val:
                    return False
                self.front_pointer = self.front_pointer.next
            return True

        return check_recursively(head)


class Solution:
    # front_pointer = None

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # self.front_pointer = head
        front_pointer = head

        def check_recursively(node: ListNode):
            if node:
                if not check_recursively(node.next):
                    return False
                if node.val != front_pointer.val:
                    return False
                if front_pointer.next:
                    front_pointer.val = front_pointer.next.val
                    front_pointer.next = front_pointer.next.next
            return True

        return check_recursively(head)


# def test_func(node:ListNode,some_node:ListNode):
#     if node:
#         test_func(node.next,some_node)
#     else:
#         some_node = ListNode(100)

class Solution:
    def reverseList(self, head: Optional[ListNode], prev_node: Optional[ListNode], stop_node=None) -> Optional[
        ListNode]:
        """MUTATING"""
        if head is None:
            return
        current_node = head
        previous_node = prev_node
        while current_node is not stop_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node

        return previous_node

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        counter = 1
        node = head
        while node:
            if node.next:
                counter += 1
            last_node = node
            node = node.next

        # last_node = node
        middle = counter // 2
        counter = 1
        node = head
        # previous_node = None

        while node:
            if counter < middle:
                node = node.next
                counter += 1
            elif counter == middle:
                middle_node = node
                self.reverseList(node.next, node)
                break

        # node = head
        counter = 1
        left = head
        right = last_node
        while counter <= middle:
            if left.val != right.val:
                self.reverseList(last_node, None, middle_node)
                return False
            left = left.next
            right = right.next
            counter += 1

        self.reverseList(last_node, None, middle_node)
        return True


if __name__ == '__main__':
    s = Solution()
    node1 = ListNode(1)
    node2 = ListNode(1)
    node3 = ListNode(2)
    node4 = ListNode(1)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    # test_func(node1,node1)
    print(s.isPalindrome(node1))
    a = 1
    # print(s.isPalindrome(node1))
