import createBinaryTree
def numberOfLeaf(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    leftNode=numberOfLeaf(root.left)
    rightnode=numberOfLeaf(root.right)
    return leftNode+rightnode