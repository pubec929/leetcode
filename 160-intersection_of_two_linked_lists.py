"""https://leetcode.com/problems/intersection-of-two-linked-lists/description/"""
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seen = set()

        nodeA, nodeB = headA, headB
        while nodeA or nodeB:
            if nodeA:
                addrA = id(nodeA)
                if addrA in seen:
                    return nodeA
                seen.add(addrA)
                nodeA = nodeA.next
            if nodeB:
                addrB = id(nodeB)
                if addrB in seen:
                    return nodeB
                seen.add(addrB)
                nodeB = nodeB.next

        return ListNode(0)
