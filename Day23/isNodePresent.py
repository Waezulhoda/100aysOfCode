import createBinaryTree #for getting this py file go to Day21
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
root=createBinaryTree.takeInput()
print(isNodePresent(root,int(input("ENter the value of k: "))))