# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        val_map = {}
        counter = 0
        while head:
            if head.val in val_map:
                return True
            else:
                val_map[head.val] = counter
            counter+=1
            head = head.next
        return False