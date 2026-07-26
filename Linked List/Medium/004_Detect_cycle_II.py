# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        maps= set()

        temp = head
        while temp:
            if temp in maps:
                return temp
            maps.add(temp)
            temp = temp.next
        return None
