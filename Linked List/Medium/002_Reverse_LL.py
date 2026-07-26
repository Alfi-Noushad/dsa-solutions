class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Solution:
    def reverse(self,head):
        prev = None
        current = head
        while current:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode

        return prev
    def pRint(self,prev):
        temp = prev
        while temp:
            print(temp.data)
            temp = temp.next
s = Solution()
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

a = s.reverse(head)
s.pRint(a)
