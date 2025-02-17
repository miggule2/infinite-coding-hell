class Solution(object):
    # linked list 뒤집기
    def reverse(self, head):
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev
    
    def linkedListToList(self, node):
        lst = []
        while node:
            lst.append(node.val)
            node = node.next
        return lst

    def ListToRevrsedLL(self, result):
        prev = None
        for r in result:
            node = ListNode(int(r))  # 숫자로 변환하여 ListNode 생성
            node.next = prev
            prev = node
        return node
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        a = self.linkedListToList(self.reverse(l1))
        b = self.linkedListToList(self.reverse(l2))

        result = int(''.join(str(e) for e in a)) + int(''.join(str(e) for e in b))

        return self.ListToRevrsedLL(str(result))
