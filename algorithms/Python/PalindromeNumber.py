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
            
        count = 0
        temp = x
        while(temp>0):
            temp = temp/ 10
            count += 1
        
        for i in range(count-1, 0, -2):

            
            if x%10 != int(x/math.pow(10, i)):
                return False
         
            x =int ( x%math.pow(10, i)/10)
        return True

'''
I didn't notice that it wrote that "Do this without extra space."
So I try another way.

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
'''
