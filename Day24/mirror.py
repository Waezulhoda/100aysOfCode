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
def mirror(root):
    if root is None:
        return None
    leftNode=mirror(root.left)
    rightNode=mirror(root.right)
    root.left=rightNode #if we right rn,ln=ln,rn but root.left is still have the same address na
    root.right=leftNode
    return root #if we will not return leftNode and rightNode will Only have None in every funct call
# root=takeInput()
# printBinaryTree(root)
# mirror(root)
# printBinaryTree(root)