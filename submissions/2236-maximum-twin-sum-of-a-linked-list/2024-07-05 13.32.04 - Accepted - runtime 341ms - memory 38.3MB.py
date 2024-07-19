# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        #use fast and slow method to find the middle
        dummy = head
        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        middle = slow
        #reverse the second half so that the twin of the node is always n/2 nodes apart
        

        #edge case only two nodes
        if not middle.next:
            return dummy.val+ middle.val

        '''save our head, nextnode, prev'''
        prev = None
        curr= middle
        while curr:
            next_node = curr.next
            curr.next = prev

            prev = curr
            curr= next_node
        
        #found the middle, reversed second half now i want to move evry n/2 and n add find theeir sums
        #how do i make first half point to reversed second half
        biggerTwinSum = 0
        fast = prev #will start at the reversed second half
        slow = dummy #saved head of list in dummy variable
        
        while fast:
            biggerTwinSum = max(biggerTwinSum, slow.val + fast.val)
            slow = slow.next
            fast = fast.next
           
        return biggerTwinSum

        

