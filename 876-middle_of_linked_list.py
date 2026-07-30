"""https://leetcode.com/problems/middle-of-the-linked-list/"""
from typing import Optional

class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def arrayToList(array: list):
    if not array:
        return None
    head = ListNode(array[0])
    node = head
    for val in array[1:]:
        node.next = ListNode(val)
        node = node.next

    return head

def getLength(head: Optional[ListNode]):
    if not head:
        return 0
    length = 1
    node = head
    while node.next:
        node = node.next
        length += 1

    return length

class Solution:
    def middleNote(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        length = getLength(head)
        pos = length // 2
        """
        i = 0
        node = head
        while i < pos:
            i += 1
            node = node.next
        """
        node = head
        for _ in range(pos):
            node = node.next
        return node


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5]
    head = arrayToList(array)
    sol = Solution()
    node = sol.middleNote(head)
    print(node.val)