from typing import Optional
from rich import print

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def arrayToTree(array: list) -> Optional[TreeNode]:
    if not array:
        return None

    root = TreeNode(array[0])

    def _setNodes(nodes: list[TreeNode], vals: list):
        for i, node in enumerate(nodes):
            node.left = vals[i*2]
            node.right = vals[i*2+1]
            

    def _totree(depth, numNodes, i, nodes):
        if i >= len(array):
            return
        vals = array[i:i + 2**numNodes]
        _setNodes(nodes, vals)
        numNodes = 0
        for val in vals:
            if val is not None:
                numNodes += 1
        _totree(depth + 1, numNodes, i + len(vals), nodes)

    _totree(1, 1, 1, root)
    return root

   
if __name__ == "__main__":
    array = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]

    print(arrayToTree(array))