import queue
q1=queue.LifoQueue()
q2=queue.LifoQueue()
def reverseStack(q1,q2):
    if q1.empty():
        return q1
    ele=q1.get()
    reverseStack(q1,q2)
    while q1.empty() is False:
        q2.put(q1.get())
    q1.put(ele)
    while q2.empty() is False:
        q1.put(q2.get())
    return q1
while True:
    x=int(input())
    if x==-1:
        break
    q1.put(x)
output=reverseStack(q1,q2)
while output.empty() is False:
    print(output.get())