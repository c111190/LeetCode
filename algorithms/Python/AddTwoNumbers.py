'''
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None: return l2
        if l2 == None: return l1

        ans = ListNode(0)
        r = ans
        c = 0

        while l2:

            if not l1:
                l1 = ListNode(0)
            suml = l1.val + l2.val + c
            r.next = ListNode(suml % 10)
            c = suml / 10

            l2 = l2.next;
            r = r.next;
            l1 = l1.next

        while l1:
            suml = l1.val + c
            r.next = ListNode(suml % 10)
            c = suml / 10
            l1 = l1.next;
            r = r.next

        if c != 0:
            r.next = ListNode(c)

        return ans.next