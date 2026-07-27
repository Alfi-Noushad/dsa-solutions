# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        if head is None:
            return None
        if head.next is None:
            return head

        mid = self.findMiddle(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left,right)
        
    def findMiddle(self,head):
        slow = fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None

        return slow
    
    def merge(self,left,right):
        dummy = ListNode(0)
        temp = dummy

        while left and right:
            if left.val < right.val:
                temp.next = left
                left = left.next
            else:
                temp.next = right
                right = right.next
            temp = temp.next

        if left:
            temp.next = left
        else:
            temp.next = right
            
        return dummy.next
