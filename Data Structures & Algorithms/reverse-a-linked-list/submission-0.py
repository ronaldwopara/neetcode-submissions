# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Track
        track = []
        while head:
            track.append(head.val)
            head = head.next
        
        # Step 2: reverse values
        track = track[::-1]
        
        # Step 3: build new list from reversed values
        n = ListNode(0)
        current = n
        for val in track:
            current.next = ListNode(val)
            current = current.next
        
        return n.next

        

