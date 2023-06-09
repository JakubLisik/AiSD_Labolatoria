import random

class Queue():
    def __init__(self):
        self.items = [None] * 7

    head = 0

    tail = 0

    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, item):
        try:
            self.items[self.tail] = item
            self.tail += 1
        except:
            self.items[0] = item
            self.tail = 1

    def dequeue(self):
        self.items.insert(self.head, None)
        self.head += 1
        if self.head > len(self.items)-2:
            self.head = 0
            return self.items.pop(len(self.items)-1)
        else:
            return self.items.pop(self.head)
    
    def size(self):
        return len(self.items)
    

def hotPotato():
    q = Queue()
    q.enqueue('Bill')
    q.enqueue('David')
    q.enqueue('Susan')
    q.enqueue('Jane')
    q.enqueue('Kent')
    q.enqueue('Brad')
    while q.items.count(None) != q.size()-1:
        passes = random.randint(2,12)
        for i in range(passes):
            q.enqueue(q.dequeue())
            # print(q.items)
        print("Odpada: ", q.dequeue())

    return q.dequeue()

    


print("Zwycięzcą jest: ", hotPotato())