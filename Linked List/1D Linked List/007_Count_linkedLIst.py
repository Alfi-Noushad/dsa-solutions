class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

arr = [2,4,6,8,10]
head = Node(arr[0])
current = head

for i in range(1,len(arr)):
    current.next = Node(arr[i])
    current = current.next


#traverse
temp = head
count = 0

while temp:
    print(f"->{temp.data}",end = "")
    temp = temp.next
    count+=1
print(count)