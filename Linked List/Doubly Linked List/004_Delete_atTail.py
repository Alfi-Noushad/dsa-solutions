class Node:
    def __init__(self,data,next = None,prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class Solution:
    def deleteAtTail(self,head):
        if head is None:
            return None

        # Only one node
        if head.next is None:
            return None

        temp = head

        while temp.next.next:
            temp = temp.next

        temp.next.prev = None
        temp.next = None

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


head = s.deleteAtTail(head)

s.printDl(head)