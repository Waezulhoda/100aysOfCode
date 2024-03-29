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
def printSibling(root):
    if root is None:
        return
    if root.left is not None and root.right is None:
        print(root.left.data,end=' ')  #if i return here it simply means I don't want to
        #find any other nodes with this node. use the example 
        #(1 2 3 4 -1 -1...till the end of bt)
    if root.left is None and root.right is not None:
        print(root.right.data,end=' ')
    leftNode=printSibling(root.left)
    rightNode=printSibling(root.right)
root=takeInput()
printSibling(root)