import createBinaryTree #for getting this py file go to Day21
def printNodeAtDepth(root,k):
    if k<0 or root is None:
        return
    if k==0:
        if root is not None:
            print(root.data)
    leftNode=printNodeAtDepth(root.left,k-1)
    rightNode=printNodeAtDepth(root.right,k-1)
root=createBinaryTree.takeInput()
printNodeAtDepth(root,int(input("enter the value of K: ")))