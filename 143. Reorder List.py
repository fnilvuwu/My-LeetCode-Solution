# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # step-by-step thought process (atleast in my head as of now)
        # 1. find the middle of the linked list
        # 2. reverse the second half of the linked list
        # 3. merge the two linked lists
        def find_middle(head):
            slow = head
            fast = head
            while fast is not None and fast.next is not None:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        def reverse_linked_list(head):
            current = head
            previous = None
            while current is not None:
                next_node = current.next
                current.next = previous
                previous = current
                current = next_node
            return previous
        
        def merge_linked_lists(head1, head2):
            while head2 is not None:
                temp1 = head1.next
                temp2 = head2.next
                head1.next = head2
                head2.next = temp1
                head1 = temp1
                head2 = temp2
        
        if head is None:
            return None
        
        middle = find_middle(head)

        head1 = head

        head2 = middle.next
        middle.next = None

        head2 = reverse_linked_list(head2)

        merge_linked_lists(head1, head2)
# Time complexity: O(N)
# Space complexity: O(1)