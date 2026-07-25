class Node:
    def __init__(self,data,next = None,prev = None):
        self.data = data
        self.next = next
        self.prev = prev
class Solution:
    def reverse(self,head):
        if head is None:
            return None
        temp = head
        new_head = None

        while temp:
            a = temp.next
            temp.next = temp.prev
            temp.prev = a

            new_head = temp

            temp = temp.prev
        
        return new_head
    def printDll(self,head):
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
print("before :     ",end ="")
s.printDll(head)
head = s.reverse(head)
print("after :     ",end ="")
s.printDll(head)
