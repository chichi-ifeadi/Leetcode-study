# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        #save head
        dummy = ListNode(0, head)
        leftPrev,  curr = dummy, head
        #to get the node that starts the left
        for _ in range(left-1):
            leftPrev, curr= curr, curr.next  
        prev = None
        #reverse using length of a sublist
        for _ in range(right-left+1):
            next_node = curr.next
            curr.next = prev
            prev, curr = curr, next_node
            
        #change what the leftmost prev node points to and what the initial left points to
        
        leftPrev.next.next = curr
        leftPrev.next = prev
        
        return dummy.next
        