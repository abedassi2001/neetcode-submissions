# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        iter_1 = list1
        iter_2 = list2 
        new_start = ListNode(0)
        ret_node = new_start
        while iter_1 and iter_2 :

            if iter_2.val < iter_1.val :
                new_start.next = iter_2
                iter_2 = iter_2.next

                
            else :
                new_start.next = iter_1
                iter_1 = iter_1.next

            new_start = new_start.next
            
        if iter_1 :
            new_start.next = iter_1 
        if iter_2 :
            new_start.next = iter_2 

        return ret_node.next            
            
