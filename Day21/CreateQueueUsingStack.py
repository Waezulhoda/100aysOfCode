#   1st method.. enqueue O(n).. dequeue and front O(1)   #

class QueueUsingStack1:
    def __init__(self):
        self.__stack1=[]
        self.__stack2=[]
    def enqueue(self,data):
        while len(self.__stack1)!=0:
            self.__stack2.append(self.__stack1.pop())
        self.__stack1.append(data)
        while len(self.__stack2)!=0:
            self.__stack1.append(self.__stack2.pop())
    def dequeue(self):
        if self.isEmpty():
            return -1
        return self.__stack1.pop()
    def front(self):
        if self.isEmpty():
            print("stack is empty")
        return self.__stack1[-1]
    def size(self):
        return len(self.__stack1)
    def isEmpty(self):
        return self.size()==0
# q=QueueUsingStack1()
# q.enqueue(10)
# q.enqueue(20)
# q.enqueue(30)
# q.enqueue(40)
# q.enqueue(50)
# while not q.isEmpty():
#     print(q.dequeue())

#  1st method.. enqueue O(1).. dequeue and front O(n)   #

class QueueUsingStack2:
    def __init__(self):
        self.__stack1=[]
        self.__stack2=[]
    def enqueue(self,data):
        self.__stack1.append(data)
    def dequeue(self):
        if self.isEmpty():
            return -1
        while len(self.__stack1)!=1:
            self.__stack2.append(self.__stack1.pop())
        element=self.__stack1.pop()
        while len(self.__stack2)!=0:
            self.__stack1.append(self.__stack2.pop())
        return element
    def front(self):
        if self.isEmpty():
            print("stack is empty")
        while len(self.__stack1)!=1:
            self.__stack2.append(self.__stack1.pop())
        element=self.__stack1[-1]
        while len(self.__stack2)!=0:
            self.__stack1.append(self.__stack2.pop())
        return element
    def size(self):
        return len(self.__stack1)
    def isEmpty(self):
        return self.size()==0
# q=QueueUsingStack2()
# q.enqueue(10)
# q.enqueue(20)
# q.enqueue(30)
# q.enqueue(40)
# q.enqueue(50)
# while not q.isEmpty():
#     print(q.front())
#     print(q.dequeue())