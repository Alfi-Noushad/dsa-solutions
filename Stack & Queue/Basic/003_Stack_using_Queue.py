class MyStack(object):

    def __init__(self, size=1000):
        self.queueArray = [0] * size
        self.capacity = size
        self.front = 0
        self.rear = -1

    def push(self, x):
        if self.rear == self.capacity - 1:
            return False

        # Add the new element at the rear
        self.rear += 1
        self.queueArray[self.rear] = x

        # Rotate the previous elements behind the new element
        old_size = self.rear - self.front

        for _ in range(old_size):
            val = self.queueArray[self.front]

            # Shift everything one position to the left
            for i in range(self.front, self.rear):
                self.queueArray[i] = self.queueArray[i + 1]

            self.queueArray[self.rear] = val

        return True

    def pop(self):
        if self.front > self.rear:
            return -1

        value = self.queueArray[self.front]
        self.front += 1

        return value

    def top(self):
        if self.front > self.rear:
            return -1

        return self.queueArray[self.front]

    def empty(self):
        return self.front > self.rear


if __name__ == "__main__":
    stack = MyStack()

    commands = ["MyStack", "push", "push", "top", "pop", "empty"]
    inputs = [[], [1], [2], [], [], []]

    for i in range(len(commands)):
        if commands[i] == "push":
            stack.push(inputs[i][0])
            print("null", end=" ")

        elif commands[i] == "pop":
            print(stack.pop(), end=" ")

        elif commands[i] == "top":
            print(stack.top(), end=" ")

        elif commands[i] == "empty":
            print("true" if stack.empty() else "false", end=" ")
