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
def NumOfNodesGreaterThanX(root,x):
    if root is None:
        return 0
    leftNode=NumOfNodesGreaterThanX(root.left,x)
    rightNode=NumOfNodesGreaterThanX(root.right,x)
    if root.data>x:
        return 1+leftNode+rightNode
    else:
        return leftNode+rightNode
root=takeInput()
print(NumOfNodesGreaterThanX(root,int(input("Enter the value of x: "))))