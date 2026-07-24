class Node:
    def __init__(self,data,next = None,prev = None):
        self.data = data
        self.next = next
        self.prev = prev

arr = [2,4,6,7,8]

head = Node(arr[0])

print(head)

print(head.data)
print(head.prev)
print(head.next)