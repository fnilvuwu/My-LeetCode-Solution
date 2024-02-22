# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def printLinkedList(head):
    myList = []
    current = head
    while current is not None:
        myList.append(current.val)
        current = current.next

    return myList

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        list1 = printLinkedList(l1)
        list2 = printLinkedList(l2)
        num1 = int("".join(map(str, list1[::-1])))
        num2 = int("".join(map(str, list2[::-1])))
        sum = ",".join(str(num1+num2)[::-1])
        return ListNode(sum)