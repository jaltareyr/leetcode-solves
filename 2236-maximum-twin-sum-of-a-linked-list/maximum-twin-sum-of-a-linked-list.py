# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """

        from collections import deque

        stack = deque()

        while head:
            stack.append(head)
            head = head.next
        summ = 0
        while stack:
            summ = max(summ, (stack.pop().val + stack.popleft().val))
        return summ
        
