class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        
        p1, p2 = head, head.next
        head.next = None
        
        while p2:
            if p2.next:
                tmp = p2.next
                p2.next = p1
                p1 = p2
                p2 = tmp
            else:
                p2.next = p1
                return p2