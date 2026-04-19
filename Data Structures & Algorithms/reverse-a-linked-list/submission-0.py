# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ret_head = head
        if head is None :
            return None
        while ret_head.next :
            ret_head = ret_head.next
                        
        self.Helper(head,ret_head) 
        return ret_head


    def Helper(self,head , ret_head) :
        if head.next is None : 
            ret_head = head 
            return head 

        next_head = self.Helper(head.next , ret_head)
        head.next = None
        next_head.next = head

        return head

