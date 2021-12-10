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
def middle(head):
    slow=head
    fast=head
    while (fast.next is not None) and (fast.next.next is not None):
        slow=slow.next
        fast=fast.next.next
    return slow.data
head=takeInput()
print(f"Middle Node is {middle(head)}")