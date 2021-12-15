##########   create Queue with List   ##########

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
q1=QueueUsingList()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
while q1.isEmpty() is False:
    print(q1.front())
    q1.dequeue()

##########   create Queue with LL   ##########

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class queueUsingLL:
    def __init__(self):
        self.__head=None
        self.__tail=None
        self.__count=0
    def enqueue(self,element):
        newNode=Node(element)
        if self.__head is None:
            self.__head=newNode
            self.__tail=newNode
            self.__count+=1
        else:
            self.__tail.next=newNode
            self.__tail=newNode
            self.__count+=1
    def dequeue(self):
        if self.__head is None:
            print("queue is Empty")
            return
        element=self.__head
        self.__head=self.__head.next
        self.__count-=1
        return element.data
    def front(self):
        if self.__head is None:
            print("queue is empty")
            return
        return self.__head.data
    def size(self):
        return self.__count
    def isEmpty(self):
        return self.size()==0
q1=queueUsingLL()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
while q1.isEmpty() is False:
    print(q1.dequeue())