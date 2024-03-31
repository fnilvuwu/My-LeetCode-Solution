# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def to_array(node):
            array = []
            current = node
            while current:
                array.append(current.val)
                current = current.next
            return array

        def subArrayExists(arr):
            prefix_sum = 0
            seen = set()
            for num in arr:
                prefix_sum += num
                if prefix_sum in seen or prefix_sum == 0:
                    return True
                seen.add(prefix_sum)
            return False
 
        def removeZeroSumSubArray(arr):
            prefix_sum = 0
            prefix_sums = {0: -1}  # Initialize prefix sum with 0 at index -1
            for i, num in enumerate(arr):
                prefix_sum += num
                if prefix_sum in prefix_sums:
                    # Remove elements from prefix_sums[prefix_sum] + 1 to i
                    arr = arr[:prefix_sums[prefix_sum] + 1] + arr[i + 1:]
                    return arr
                prefix_sums[prefix_sum] = i
            return arr

        def to_linked_list(arr):
            dummy = ListNode(0)
            current = dummy
            for val in arr:
                current.next = ListNode(val)
                current = current.next
            return dummy.next

        array = to_array(head)
        while subArrayExists(array):
            array = removeZeroSumSubArray(array)

        return to_linked_list(array)
