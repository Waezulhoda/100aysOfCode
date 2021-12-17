import createBinaryTree as cbt
def largestNodeData(root):
    if root is None:
        return -1
    leftnode=largestNodeData(root.left)
    rightNode=largestNodeData(root.right)
    largest=max(root.data,leftnode,rightNode)
    return largest
root=cbt.takeInput()
print(largestNodeData(root))