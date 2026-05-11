class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        iter_slow = head 
        iter_fast = head.next 

        while iter_fast and iter_fast.next   :
            iter_slow = iter_slow.next
            iter_fast = iter_fast.next.next 

        past_node = None 
        after_node = iter_slow

        while iter_slow != None :
            after_node = iter_slow.next
            iter_slow.next = past_node 
            past_node = iter_slow
            iter_slow = after_node 

        save_head = head
        while head :

            save_right = head.next 
            save_left = past_node.next 
            head.next = past_node
            past_node.next = save_right
            head = save_right 
            past_node = save_left

        return None







             
