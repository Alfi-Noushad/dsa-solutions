# Definition for singly-linked list.
class ListNode(object):
   def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class solution:
    def sortList(self,head):

        zeroHead = ListNode(0)
        oneHead = ListNode(0)
        twoHead = ListNode(0)


        zero = zeroHead
        one = oneHead
        two = twoHead

        temp = head
        while temp:
            if temp.val == 0:
                zero.next = temp
                zero = zero.next
            elif temp.val == 1:
                one.next = temp
                one = one.next
            else:
                two.next= temp
                two = two.next

            temp = temp.next

        zero.next = oneHead.next if oneHead.next else twoHead.next

        one.next = twoHead.next

        two.next = None

        if zeroHead.next:
            return zeroHead.next

        elif oneHead.next:
            return oneHead.next

        else:
            return twoHead.next