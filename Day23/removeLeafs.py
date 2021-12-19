class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def takeInput():
    data=int(input())
    if data==-1:
        return None
    root=BinaryTreeNode(data)
    root.left=takeInput()
    root.right=takeInput()
    return root
def printBinaryTree(root):
    if root is None:
        return
    print(root.data,end=': ')
    if root.left is not None:
        print(f"L->{root.left.data}",end=', ')
    if root.right is not None:
        print(f"R->{root.right.data}",end=' ')
    print()
    printBinaryTree(root.left)
    printBinaryTree(root.right)

def removeLeaf(root):
    if root is None:
        return None
    if root.left is None and root.right is None:
        return None
    root.left=removeLeaf(root.left)
    root.right=removeLeaf(root.right)
# root=takeInput()
# removeLeaf(root)
# printBinaryTree(root)