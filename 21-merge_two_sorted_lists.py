from rich import print
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def loop(head: ListNode):
    node = head
    i = 0
    while node is not None:
        print(i, node.val)
        node = node.next
        i += 1

def arrayToList(array: list) -> Optional[ListNode]:
    if not array:
        return None
    head = ListNode(array[0])
    node = head
    for val in array[1:]:
        newNode = ListNode(val)
        node.next = newNode
        node = newNode
    return head

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]):
        l, r = list1, list2
            
        if l is None or r is None:
            return l or r
        if l.val < r.val:
            head = l
            l = l.next
        else:
            head = r
            r = r.next
        node = head
        while True:
            if l is None and r is None:
                break

            if l is None:
                newNode = ListNode(r.val)
                node.next = newNode
                node = node.next
                r = r.next
                continue

            if r is None:
                newNode = ListNode(l.val)
                node.next = newNode
                node = node.next
                l = l.next
                continue
            if l.val < r.val:
                newNode = ListNode(l.val)
                node.next = newNode
                node = node.next
                l = l.next

            else:
                newNode = ListNode(r.val)
                node.next = newNode
                node = node.next
                r = r.next

        return head

if __name__ == "__main__":
    list1 = arrayToList([1, 2, 4])
    list2 = arrayToList([1, 3, 4])
    sol = Solution()
    node = sol.mergeTwoLists(list1, list2)
    loop(node)
