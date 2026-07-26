class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Solution:
    def findMiddle(self,head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

s = Solution()
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

a = s.findMiddle(head)
print(a.data)
