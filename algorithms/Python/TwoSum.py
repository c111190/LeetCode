'''
# 1.Two Sum
#
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution.
#
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_t = sorted(nums)

        for idx, x in enumerate(nums_t):
            for idy, y in enumerate(nums_t[idx+1:]):
                n = x + y
                if n == target:
                    n1 = nums.index(x)
                    if x == y:
                        return [n1, (n1+1+nums[n1+1:].index(y))]
                        
                    return [n1, nums.index(y)]
        return []