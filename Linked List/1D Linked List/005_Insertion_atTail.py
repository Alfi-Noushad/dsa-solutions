class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Solution:
    def insertAtTail(self,newData,head):
        newNode = Node(newData)
        if head is None:
            return newNode

        temp = head
        #traverse
        while temp.next != None:
            temp = temp.next
        temp.next = newNode
             
        
    def printList(self,head):
        temp = head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


s = Solution()
head = Node(2)
head.next = Node(3)
head.next.next = Node(4)

print("Original List:", end=" ")
s.printList(head)

#inserting new node at head
s.insertAtTail(5,head)
print("New List:", end=" ")
s.printList(head)