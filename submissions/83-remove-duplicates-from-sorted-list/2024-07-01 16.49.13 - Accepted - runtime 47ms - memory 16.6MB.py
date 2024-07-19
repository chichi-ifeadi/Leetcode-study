# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        end = head
    
        while end and end.next:
            if end.val == end.next.val:
                end.next = end.next.next
            else:    
                end = end.next
            
            
        return head