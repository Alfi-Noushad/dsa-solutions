class Node:
    def __init__(self,data,next = None,prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class Solution:
    def insertAtTail(self,head,newval):
        newNode = Node(newval)

        if head is None:
            return newNode
        
        temp = head

        while temp.next:
            temp =  temp.next
        
        temp.next = newNode
        newNode.prev = temp

        return head

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


head = s.insertAtTail(head,5)

s.printDl(head)