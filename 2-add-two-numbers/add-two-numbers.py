# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        result = ListNode()
        current = result

        tenth = 0

        while l1 or l2 or tenth:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            addition = val1 + val2 + tenth
            tenth = addition//10
            current.next = ListNode(addition%10)

            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return result.next