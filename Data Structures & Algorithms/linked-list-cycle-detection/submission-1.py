# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        seen = set()
        while curr:
            if curr in seen:      # already visited this node → cycle
                return True
            seen.add(curr)        # mark current node as visited
            curr = curr.next      # move to next
        return False              # reached the end → no cycle


        