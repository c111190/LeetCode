'''
# 9. Palindrome Number
# Determine whether an integer is a palindrome. Do this without extra space.
#
# https://leetcode.com/problems/palindrome-number/
'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
            
        num = str(x)
        mid = float(len(num)-1)/2

        for i in range(int(math.ceil(mid))+1):
            f = int(math.floor(mid+i))
            c = int(math.ceil(mid-i))
            print(f)
            print(c)
            if num[f] != num[c]:
                return False
 
        return True
