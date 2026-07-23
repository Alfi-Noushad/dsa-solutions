class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Solution:
    def insertAtHead(self,newData,head):
        newNode = Node(newData)
        newNode.next = head
        head = newNode
        return head

    def printList(self,head):
        temp = head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

s = Solution()
head = Node(2)
head.next = Node(3)

print("Original List:", end=" ")
s.printList(head)

#inserting new node at head
head = s.insertAtHead(1,head)
print("New List:", end=" ")
s.printList(head)