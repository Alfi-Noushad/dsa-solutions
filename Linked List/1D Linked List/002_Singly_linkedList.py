class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

arr = [2,4,6,8]
head = Node(arr[0])
current = head

for i in range(1,len(arr)):
    current.next = Node(arr[i])
    current = current.next

temp = head

while temp:
    print(temp.data)
    print(temp.next)
    temp = temp.next