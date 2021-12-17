import createBinaryTree
def numOfNodes(root):
    if root is None:
        return 0
    leftCount=numOfNodes(root.left)
    rightCount=numOfNodes(root.right)
    return 1+leftCount+rightCount
root=createBinaryTree.takeInput()
createBinaryTree.printBinaryTree(root)
print(numOfNodes(root))