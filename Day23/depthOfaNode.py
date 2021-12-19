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
def printNodeAtDepth(root,k):
    if k<0 or root is None:
        return
    if k==0:
        if root is not None:
            print(root.data)
    leftNode=printNodeAtDepth(root.left,k-1)
    rightNode=printNodeAtDepth(root.right,k-1)
# root=takeInput()
# printNodeAtDepth(root,int(input("enter the value of K: ")))