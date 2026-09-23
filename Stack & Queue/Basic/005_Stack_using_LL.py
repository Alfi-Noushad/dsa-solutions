class Node:
     def __init__(self,data,next = None):
            self.data = data
            self.next = next

class LinkedListStack:
    def __init__(self):
        self.top = None

    def push(self, x):
        newNode = Node(x)
        newNode.next = self.top
        self.top = newNode
         

    def pop(self):
        if self.top == None:
            return None
        pop_val = self.top
        self.top = self.top.next
        return pop_val.data

    def tops(self):
        return self.top.data

    def isEmpty(self):
        return self.top is None


if __name__ == "__main__":
    stack = LinkedListStack()

    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Top:", stack.tops())

    print("Pop:", stack.pop())
    print("Top:", stack.tops())

    print("Is empty:", stack.isEmpty())