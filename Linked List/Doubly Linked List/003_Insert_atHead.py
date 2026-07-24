class Node:
    def __init__(self,data,next = None,prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class Solution:
    def insertAtHead(self,head,newval):
        newNode = Node(newval)
        newNode.next = head
        head = newNode

        if head is not None:
            head.prev = newNode
        return newNode

    def printDl(self,head):
        temp = head
        print(None,"<->",end="")
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print(None)

s = Solution()

head = Node(1)

second = Node(2)
third = Node(3)

head.next = second
second.prev = head

second.next = third
third.prev = second


head = s.insertAtHead(head,5)

s.printDl(head)