from CreateQueueUsingStack import QueueUsingStack1
def reverseQueue(queue):
    if queue.isEmpty():
        return queue
    firstElement=queue.dequeue()
    smallstack=reverseQueue(queue)
    smallstack.enqueue(firstElement)
    return smallstack
queue=QueueUsingStack1()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
queue.enqueue(60)
solution=reverseQueue(queue)
while not solution.isEmpty():
    print(solution.dequeue())