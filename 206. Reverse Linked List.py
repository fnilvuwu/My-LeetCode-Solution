# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        reverse_list = []
        
        while current is not None:
            reverse_list.append(current.val)
            current = current.next
        
        reverse_list.reverse()
        
        reverse_linkedlist = ListNode()
        current = reverse_linkedlist
        for val in reverse_list:
            current.next = ListNode(val)
            current = current.next
        
        return reverse_linkedlist.next