"""https://leetcode.com/problems/remove-duplicates-from-sorted-list/"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def listToArray(head: ListNode):
    vals = []
    node = head
    while node:
        vals.append(node.val)
        node = node.next
    return vals

def arrayToList(array: list) -> ListNode:
    if not array:
        return ListNode()

    head = ListNode(array[0])
    node = head
    for item in array[1:]:
        node.next = ListNode(item)
        node = node.next
    return head


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        node = head
        while node and node.next:
            while node.next and node.val == node.next.val:
                node.next = node.next.next

            node = node.next
        return head
