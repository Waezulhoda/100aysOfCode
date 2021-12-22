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
def minAndMax(root):
    if root is None:
        return 10000000000000,-1
    leftOutput=minAndMax(root.left)
    rightOutput=minAndMax(root.right)
    minValue=min(root.data,leftOutput[0],rightOutput[0])
    maxValue=max(root.data,leftOutput[1],rightOutput[1])
    return minValue,maxValue
root=takeInput()
minValue,maxValue=minAndMax(root)
print(minValue,maxValue)