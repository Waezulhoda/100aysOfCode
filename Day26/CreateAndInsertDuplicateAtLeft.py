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
def createInsertDuplicate(root):
    if root is None:
        return None
    leftOutput=createInsertDuplicate(root.left)
    rightOutput=createInsertDuplicate(root.right)
    newNode=BinaryTreeNode(root.data)
    root.left=newNode
    newNode.left=leftOutput
    root.right=rightOutput
    return root
root=takeInput()
root=createInsertDuplicate(root)
printBinaryTree(root)