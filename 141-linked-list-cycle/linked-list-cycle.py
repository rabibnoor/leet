# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not (head and head.next):
            return False
        
        i = head
        j = head.next.next
        while(i and j):
            if i == j:
                return True
            i = i.next
            if not j.next:
                return False
            j = j.next.next

        return False

