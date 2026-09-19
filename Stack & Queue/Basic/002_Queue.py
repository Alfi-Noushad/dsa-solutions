class Queue:
    def __init__(self,size =1000):
        self.queueArray = [0] * size
        self.capacity = size
        self.rear = -1
        self.front = 0

    def enqueue(self,x):
        if self.rear == self.capacity -1:
            print("queue overflow ")
            return 
        self.rear +=1
        self.queueArray[self.rear] = x

    def dequeue(self):
        if self.front > self.rear:
            print("queue underflow")
            return -1
        
        
        deq_val = self.queueArray[self.front]
        self.front += 1
        return deq_val

    def display(self):
        if self.front > self.rear:
            print("queue is empty")
            return
        for i in range(self.front,self.rear+1):
            print(self.queueArray[i],end= " ")

if __name__ == "__main__":
    queue = Queue(5)

    commands = ["Queue", "enqueue", "enqueue", "enqueue", "dequeue", "display"]
    inputs = [[], [10], [20], [30], [], []]

    for i in range(len(commands)):
        if commands[i] == "Queue":
            print("null", end=" ")

        elif commands[i] == "enqueue":
            queue.enqueue(inputs[i][0])
            print("null", end=" ")

        elif commands[i] == "dequeue":
            print(queue.dequeue(), end=" ")

        elif commands[i] == "display":
            queue.display()