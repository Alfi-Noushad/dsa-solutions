class Node:
     def __init__(self,data,next = None):
            self.data = data
            self.next = next

class LinkedListQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, x):
        newNode = Node(x)
        if self.front is None:
             self.rear = newNode
             self.front = newNode
        else:
             self.rear.next = newNode
        self.rear = newNode
        

    def dequeue(self):
        if self.front is None:
             self.front = None
             return None
        deq_val = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return deq_val
    
    def peek(self):
        if self.front is None:
            return None
        return self.front.data
     

    def isEmpty(self):
         return self.front is None

if __name__ == "__main__":
    queue = LinkedListQueue()

    print("Empty:", queue.isEmpty())

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    print("Peek:", queue.peek())

    print("Dequeue:", queue.dequeue())
    print("Dequeue:", queue.dequeue())

    print("Peek:", queue.peek())

    print("Dequeue:", queue.dequeue())

    print("Empty:", queue.isEmpty())