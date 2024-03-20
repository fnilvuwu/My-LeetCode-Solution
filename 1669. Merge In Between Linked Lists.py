# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # Find the node before index a
        prev_a = list1
        for _ in range(a - 1):
            prev_a = prev_a.next
        
        # Find the node after index b
        after_b = prev_a
        for _ in range(b - a + 2):
            after_b = after_b.next
        
        # Connect the node before a to the head of list2
        prev_a.next = list2
        
        # Find the end of list2
        end_list2 = list2
        while end_list2.next:
            end_list2 = end_list2.next
        
        # Connect the end of list2 to the node after b
        end_list2.next = after_b
        
        return list1
