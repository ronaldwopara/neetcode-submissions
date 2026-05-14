# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = []
        curr1, curr2 = list1, list2
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                result.append(curr1.val)
                curr1 = curr1.next
  
            else:
                result.append(curr2.val)
                curr2 = curr2.next
                
        while curr1:
            result.append(curr1.val)
            curr1 = curr1.next
        while curr2:
            result.append(curr2.val)
            curr2 = curr2.next
        
        dummy = ListNode(0)
        current = dummy
        for val in result:
            current.next = ListNode(val)
            current = current.next
        
        return dummy.next
        
        