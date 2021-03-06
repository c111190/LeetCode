#788. Rotated Digits
'''
X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from X.  Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become invalid.

Now given a positive number N, how many numbers X from 1 to N are good?
'''
class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        vaild = 0

        for num in xrange(N+1):
            s = str(num)
            if '3' in s or '4' in s or '7' in s:
                continue
            if not ('2' in s or '5' in s or '6' in s or '9' in s):
                continue

            vaild += 1
                
        return vaild
