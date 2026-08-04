

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