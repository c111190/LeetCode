#442. Find All Duplicates in an Array
'''
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?
'''
import collections

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        data = collections.defaultdict(int)
        for i in nums:
            data[i] += 1
            
        b = [kv[0] for kv in data.items() if kv[1]>1]
        return b
