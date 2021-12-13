##########   creating stack with list   ##########
class StackUsingList:
    def __init__(self):
        self.__data=[]
    def push(self,item):
        self.__data.append(item)
    def pop(self):
        if self.isEmpty():
            print("stack is empty")
        return self.__data.pop()
    def top(self):
        if self.isEmpty():
            print("stack is empty")
        return self.__data[self.size()-1]
    def size(self):
        return len(self.__data)
    def isEmpty(self):
        return self.size()==0

##########   creating stack with LL   ##########
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class StackUsingLL:
    def __init__(self):
        self.__head=None
        self.__count=0
    def push(self,item):
        newNode=Node(item)
        newNode.next=self.__head
        self.__head=newNode
        self.__count=self.__count+1
    def pop(self):
        if self.isEmpty():
            print("stack is empty")
            return
        self.data=self.__head.data
        self.__head=self.__head.next
        self.__count=self.__count-1
        return self.data
    def top(self):
        if self.isEmpty():
            print("stack is empty")
            return
        return self.__head.data
    def size(self):
        return self.__count
    def isEmpty(self):
        return self.size()==0

##########   creating stack with inbuit    ##########
import queue
q=queue.LifoQueue()
q.put(10)
q.put(20)
q.put(30)
q.put(40)
while q.empty() is False:
    print(q.get())