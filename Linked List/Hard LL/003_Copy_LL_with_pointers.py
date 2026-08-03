# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        hashmp = {}

        temp = head
        while temp:
            hashmp[temp] = Node(temp.val)
            temp =temp.next
        temp = head
        while temp:
            copy = hashmp[temp]
            copy.next = hashmp[temp.next] if temp.next else None
            copy.random = hashmp[temp.random] if temp.random else None
            temp = temp.next
        
        return hashmp[head] if head else None



        