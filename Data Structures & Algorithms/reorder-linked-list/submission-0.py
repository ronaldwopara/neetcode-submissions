# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        arr = []
        while curr:
            arr.append(curr)
            curr = curr.next

        dummy_node = ListNode(0)
        prev = dummy_node   # <- this is just for stitching

        while len(arr) > 1:
            first = arr.pop(0)
            second = arr.pop()
            prev.next = first
            first.next = second
            prev = second    # move the stitch forward

        if arr:  # leftover middle node
            prev.next = arr.pop()
            prev = prev.next

        prev.next = None     # avoid cycle
        

        



        

        