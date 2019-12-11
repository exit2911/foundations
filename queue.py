import queue

L = queue.Queue(maxsize=20) # make L a queue

L.put(5) #add item to queue
L.put(4)
L.put(3)
L.put(3)
L.put(4)

print(L.get())
print(L.get())
print(L.get())
print(L.get())
print(L.get())

#underflow and overflow (queue run out of size or is empty to queue) will go on an infinite loop

#LAST IN FIRST OUT QUEUE

L = queue.LifoQueue(maxsize=6)

print(L.qsize())

L.put(5) #add item to queue
L.put(4)
L.put(3)
L.put(3)
L.put(4)

print("lifo",L.get())
print(L.get())
print(L.get())
print(L.get())
print(L.get())
                       
