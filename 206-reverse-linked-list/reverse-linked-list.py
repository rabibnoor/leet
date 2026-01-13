# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return
        cur = head.next
        head.next =None
        while(cur):
            
           # print(head.val,cur.val)
            nxt = cur.next
            cur.next = head
            head = cur
            cur = nxt
        return head
        
        
            
        