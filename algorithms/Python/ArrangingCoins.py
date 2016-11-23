'''
# 441. Arranging Coins
#
# You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.
# Given n, find the total number of full staircase rows that can be formed.
# n is a non-negative integer and fits within the range of a 32-bit signed integer.
# https://leetcode.com/problems/arranging-coins/
'''

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = int(n ** 0.5)
        n = n - sum(range(i + 1))

        while n >= 0:
            i = i + 1
            n = n-i
            
        return i-1