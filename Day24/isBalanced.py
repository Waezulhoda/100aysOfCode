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
def heightOfBt(root):
    if root is None:
        return 0
    leftNode=heightOfBt(root.left)
    rightNode=heightOfBt(root.right)
    if leftNode>rightNode:
        return 1+leftNode
    else:
        return 1+rightNode
def isBalanced(root):
    if root is None:
        return True
    lh=heightOfBt(root.left)
    rh=heightOfBt(root.right)
    if lh-rh>1 or rh-lh>1:
        return False
    leftNode=isBalanced(root.left)
    rightNode=isBalanced(root.right)
    if leftNode is True and rightNode is True:
        return True
    else:
        False
root=takeInput()
print(isBalanced(root))