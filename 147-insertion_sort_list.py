"""https://leetcode.com/problems/insertion-sort-list/description/"""
from listHelper import arrayToList, listToArray
from typing import Optional

class ListNode:
    def __init__(self, val: int, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        newHead = ListNode(head.val)
        node = head.next
        while node:
            # insert in new list
            if node.val > newHead.val:
                _prev, _next = newHead, newHead.next
                while _next and _next.val < node.val:
                    _prev, _next = _next, _next.next
                _prev.next = ListNode(node.val, _next)
            else:
                newHead = ListNode(node.val, newHead)
            
            node = node.next
        return newHead

sol = Solution()
array = [0]
sortedList = sol.insertionSortList(arrayToList(array))
print(listToArray(sortedList))
