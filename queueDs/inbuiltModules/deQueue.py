from collections import deque


newDeQueue = deque(maxlen=5)

for value in [10, 20, 30, 40, 50, 60]:
    newDeQueue.append(value)

print(newDeQueue.popleft())
print(newDeQueue)

help(deque)

