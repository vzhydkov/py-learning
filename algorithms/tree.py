"""
Maximum Depth of N-ary Tree
              1
            / | \
           3  2  4
          / \
         5  6
Input: root = [1,null,3,2,4,null,5,6]
Output: 3
"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children else []


def max_depth_recursion(root: Node) -> int:
    """
    >>> root = Node(1, children=[Node(3, children=[Node(5), Node(6)]), Node(2), Node(4)])
    >>> max_depth_recursion(root)
    3
    """
    if not root:
        return 0
    if not root.children:
        return 1
    height = []
    for node in root.children:
        height.append(max_depth_recursion(node))
    return max(height) + 1


def max_depth_bfs(root: Node) -> int:
    """
    BFS - use a queue, the last level we see will be the depth
    >>> root = Node(1, children=[Node(3, children=[Node(5), Node(6)]), Node(2), Node(4)])
    >>> max_depth_bfs(root)
    3
    """
    queue = []
    if root:
        queue.append((root, 1))
    depth = 0
    for (node, level) in queue:
        depth = level
        for child in node.children:
            queue.append((child, level+1))
    return depth


def max_depth_dfs(root: Node) -> int:
    """
    DFS - use a stack, use max to update depth
    >>> root = Node(1, children=[Node(3, children=[Node(5), Node(6)]), Node(2), Node(4)])
    >>> max_depth_dfs(root)
    3
    """
    stack = []
    if root:
        stack.append((root, 1))
    depth = 0
    while stack:
        (node, d) = stack.pop()
        depth = max(depth, d)
        for child in node.children:
            stack.append((child, d+1))
    return depth


if __name__ == "__main__":
    import doctest
    doctest.testmod()
