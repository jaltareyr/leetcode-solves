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
        
        head = l1  # Use `l1` as the result list
        carry = 0  # Initialize carry

        # Loop through both lists
        prev = None
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the sum and update carry
            addition = val1 + val2 + carry
            carry = addition // 10
            
            # Update l1 node's value or create new node if needed
            if l1:
                l1.val = addition % 10
                prev = l1
                l1 = l1.next
            else:
                prev.next = ListNode(addition % 10)
                prev = prev.next
            
            # Move l2 pointer
            if l2:
                l2 = l2.next
        
        return head
