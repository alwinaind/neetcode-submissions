# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        l1_str = str(l1.val)
        dummy_l1 = l1.next
        l2_str = str(l2.val)
        dummy_l2 = l2.next

        while dummy_l1!=None:
            l1_str+=str(dummy_l1.val)
            dummy_l1 = dummy_l1.next

        while dummy_l2!=None:
            l2_str+=str(dummy_l2.val)
            dummy_l2 = dummy_l2.next
        
        l1_str = l1_str[::-1]
        l2_str = l2_str[::-1]

        l3_str = str(int(l1_str)+int(l2_str))
        print(l3_str)
        l3 = ListNode(val=int(l3_str[-1]))
        if len(l3_str) == 1:
            return l3
        temp = l3
        for l in range(len(l3_str[:-2]), -1, -1):
            temp.next = ListNode(val=int(l3_str[l]))
            temp = temp.next
        
        return l3

