class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def takeInput():
    inputList=[int(ele) for ele in input().split(' ')]
    head=None
    tail=None
    for currData in inputList:
        if currData==-1:
            break
        newNode=Node(currData)
        if head is None:
            head=newNode
            tail=newNode
        else:
            tail.next=newNode
            tail=newNode
    return head
def nodePosition(head,data,start):
    if head is None:
        return -1
    if head.data==data:
        return start
    else:
        return nodePosition(head.next,data,start+1)
head=takeInput()
print(nodePosition(head,int(input()),0))