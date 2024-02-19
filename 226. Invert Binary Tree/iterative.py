def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    stack = [root]              # queue = collections.deque([(root)])
    while stack:                # queue
        node = stack.pop()      # queue.popleft()
        if node:
            node.left, node.right = node.right, node.left
            stack.extend([node.left, node.right])     # queue.extend
    return root
