class QueueUsingList:
    def __init__(self):
        self.__list=[]
        self.__front=0
        self.__count=0
    def enqueue(self,element):
        self.__list.append(element)
        self.__count+=1
    def dequeue(self):
        if self.isEmpty():
            return -1
        element=self.__list[self.__front]
        self.__front+=1
        self.__count-=1
        return element
    def front(self):
        if self.isEmpty():
            return -1
        return self.__list[self.__front]
    def size(self):
        return self.__count
    def isEmpty(self):
        return self.__count==0
class BinaryTree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def createBinaryTree(root):
    if root is None:
        return None
    q=QueueUsingList()
    q.enqueue(root)
    while not q.isEmpty():
        data1=int(input())
        data2=int(input())
        if data1!=-1:
            leftNode=BinaryTree(data1)
            q.enqueue(leftNode)
            q.front().left=leftNode
        if data2!=-1:
            rightNode=BinaryTree(data2)
            q.enqueue(rightNode)
            q.front().right=rightNode
        q.dequeue()
    return root
def printBinaryTree(root):
    if root is None:
        return None
    q=QueueUsingList()
    q.enqueue(root)
    while not q.isEmpty():
        a=q.dequeue()
        print(f"{a.data} :",end=' ')
        if a.left is not None:
            print(f"L->{a.left.data},",end=' ')
            q.enqueue(a.left)
        if a.right is not None:
            print(f"R->{a.right.data}",end=' ')
            q.enqueue(a.right)
        print()
# root=BinaryTree(int(input()))
# root=createBinaryTree(root)
# printBinaryTree(root)