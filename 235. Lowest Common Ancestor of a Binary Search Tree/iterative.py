def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if p.val > q.val:
        p,q = q,p
    while not p.val <= root.val <= q.val:
        if q.val < root.val:
            root = root.left
        else:
            root = root.right
    return root
