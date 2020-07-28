"""
# Maximum Depth of N-ary Tree
# Input: root = [1,null,3,2,4,null,5,6]
# Output: 3
"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Recursion:
    def max_depth(self, root: Node) -> int:
        if not root:
            return 0
        if not root.children:
            return 1
        height = []
        for node in root.children:
            height.append(self.max_depth(node))
        return max(height) + 1


# BFS - use a queue, the last level we see will be the depth
class BFS(object):
    def max_depth(self, root):
        queue = []
        if root:
            queue.append((root, 1))
        depth = 0
        for (node, level) in queue:
            depth = level
            queue += [(child, level+1) for child in node.children]
        return depth


# DFS - use a stack, use max to update depth
class DFS(object):
    def max_depth(self, root):
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
