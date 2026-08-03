# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """

        if head is None:
            return head
        length = 1

        temp = head
        while temp.next:
            length += 1
            temp = temp.next
        tail = temp

        k = k % length
        if k == 0:
            return head
        temp = head
        for i in range(length-k-1):
            temp = temp.next
        
        cut = temp
        newHead = temp.next
        cut.next = None
        tail.next = head
        head = newHead

        return head



        