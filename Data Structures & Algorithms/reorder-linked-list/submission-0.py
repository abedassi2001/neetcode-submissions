class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1. Find the middle of the list
        # Slow moves 1 step, Fast moves 2 steps
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse the second half in-place
        prev, curr = None, slow.next
        slow.next = None  # CRITICAL: Sever the connection here
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # 3. Merge the two halves
        first, second = head, prev
        while second:
            # Save the next nodes
            temp1, temp2 = first.next, second.next
            
            # Re-assign pointers to weave
            first.next = second
            second.next = temp1
            
            # Move forward
            first = temp1
            second = temp2