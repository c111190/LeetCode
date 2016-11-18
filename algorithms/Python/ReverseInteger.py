'''
# 7.Reverse Integer
# Reverse digits of an integer.
#
# Example1: x = 123, return 321
# Example2: x = -123, return -321
#
'''

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        r = 0
        sign = 1
        if x < 0:
            sign = -1
            x = x * -1
        
        while(x > 0):
            l = x % 10
            x = x / 10
            r = r * 10 + l
            
        r = r * sign
        
        max = 2147483647;
        min = -2147483647;
        if r > max or r < min:
            r = 0;
        
        return r
        