import createBinaryTree
def heightOfBt(root):
    if root is None:
        return 0
    leftNode=heightOfBt(root.left)
    rightNode=heightOfBt(root.right)
    if leftNode>rightNode:
        return 1+leftNode
    else:
        return 1+rightNode
root=createBinaryTree.takeInput()
print(heightOfBt(root))