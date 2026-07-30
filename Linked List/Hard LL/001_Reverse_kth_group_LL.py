# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head

        prevNode = dummy
        while True:
            temp = prevNode
            for i in range(k):
                if temp is None:
                    return dummy.next
                temp = temp.next
                if temp is None:
                    return dummy.next

            nextNode = temp.next

            prev = nextNode
            curr = prevNode.next

            while curr != nextNode:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            nextNode = prevNode.next

            prevNode.next = temp
            prevNode = nextNode


        
        

        