"""https://leetcode.com/problems/remove-linked-list-elements/description/"""
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

def arrayToList(array: list) -> Optional[ListNode]:
    if not array:
        return None

    head = ListNode(array[0])
    node = head
    for item in array[1:]:
        node.next = ListNode(item)
        node = node.next
    return head

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None

        l = None

        # set new head
        node = head
        while node is not None and node.val == val:
            node = node.next
        newHead = node
        if newHead is None or node is None:
            return None

        node = node.next
        l = newHead
        while node:
            if node.val == val:
                l.next = node.next
            else:
                l = l.next
            node = node.next

        return newHead

if __name__ == "__main__":
    sol = Solution()
    array = [2, 6, 6, 6, 6, 1]
    val = 6
    newList = sol.removeElements(arrayToList(array), val)
    print(listToArray(newList))
            
            
