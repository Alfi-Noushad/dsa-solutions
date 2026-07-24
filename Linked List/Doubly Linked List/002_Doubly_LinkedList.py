class Node:
    def __init__(self,data,next = None,prev = None):
        self.data = data
        self.next = next
        self.prev = prev

arr = [1,2,3,4,5,6]
head = Node(arr[0])
current = head

for i in range(1,len(arr)):
    newNode = Node(arr[i])
    current.next = newNode
    newNode.prev = current

    current = newNode  #current = current.next

#printing(traversing)
temp = head

while temp:
    print(temp.data, end=" <-> ")
    temp = temp.next

print("None")
