import createBinaryTree #for getting this py file go to Day21
def printSibling(root):
    if root is None:
        return
    if root.left is not None and root.right is None:
        print(root.left.data,end=' ')  #if i return here it simply means I don;t want to find any other nodes with this node. use the example (1 2 3 4 -1 -1...till the end of bt)
    if root.left is None and root.right is not None:
        print(root.right.data,end=' ')
    leftNode=printSibling(root.left)
    rightNode=printSibling(root.right)
root=createBinaryTree.takeInput()
printSibling(root)