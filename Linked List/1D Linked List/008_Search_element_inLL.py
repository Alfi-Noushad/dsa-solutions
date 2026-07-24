class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class Solution:
    def searchElement(self,head,x):
        temp = head
        while temp:
            if x == temp.data:
                return 1
            else:
                temp = temp.next
        return -1

s = Solution()
head = Node(2)
head.next = Node(4)
head.next.next = Node(6)
head.next.next.next = Node(8)

a = s.searchElement(head,3)
print(a)