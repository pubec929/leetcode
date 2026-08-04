"""https://leetcode.com/problems/add-two-numbers/description/"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 or not l2:
            return None

        head = ListNode((l1.val + l2.val) % 10)
        node = head
        transfer = 1 if (l1.val + l2.val) >= 10 else 0
        l1, l2 = l1.next, l2.next
        while l1 or l2:
            l, r = 0, 0
            if l1:
                l = l1.val
                l1 = l1.next
            if l2:
                r = l2.val
                l2 = l2.next
            s = l + r + transfer
            transfer = 1 if s >= 10 else 0
            node.next = ListNode(s % 10)
            node = node.next

        if transfer:
            node.next = ListNode(1)

        return head

