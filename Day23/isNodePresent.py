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
def isNodePresent(root,x):
    if root is None:
        return False
    if root.data==x:
        return True
    else:
        leftNodes=isNodePresent(root.left,x)
        rightNodes=isNodePresent(root.right,x)
        if leftNodes is True or rightNodes is True:
            return True
        return False
# root=takeInput()
# print(isNodePresent(root,int(input("ENter the value of k: "))))