# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        current = head
        actual_list = []
        
        while current is not None:
            actual_list.append(current.val)
            current = current.next

        if actual_list == actual_list[::-1]:
            return True
        
        return False
            

    
