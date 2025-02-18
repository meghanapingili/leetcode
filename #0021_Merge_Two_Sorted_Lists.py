# 21. Merge Two Sorted Lists

# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:
# Input: list1 = [], list2 = []
# Output: []

# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]

# Constraints:
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp = None
        result = None
        while l1 and l2:
            if l1.val <= l2.val:
                temp = self.insert(temp, l1)
                l1 = l1.next
            else:
                temp = self.insert(temp, l2)
                l2 = l2.next
            if result == None:
                result = temp
        while l1:
            temp = self.insert(temp, l1)
            l1 = l1.next
            if result == None:
                result = temp
        while l2:
            temp = self.insert(temp, l2)
            l2 = l2.next
            if result == None:
                result = temp
        return result

    def insert(self, temp, node):
        if temp == None:
            temp = node
        else:
            temp.next = node
            temp = temp.next
        return temp

