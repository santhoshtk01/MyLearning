from queueDs.dynamicQueue import DynamicQueue
from queueDs.circularQueue import CircularQueue
from queueDs.queueLL import Queue

# queue = DynamicQueue()
queue = CircularQueue(5)
# queue = Queue()

queue.enQueue(10)
queue.enQueue(20)
queue.enQueue(30)
queue.enQueue(40)
queue.enQueue(50)

print(queue)

while True:
    if queue.deQueue():
        continue
    else:
        break

print(queue)
