'''
# 412. Fizz Buzz
# Write a program that outputs the string representation of numbers from 1 to n.
#
# But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. 
# For numbers which are multiples of both three and five output “FizzBuzz”.
#
'''

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        nums = range(1, n+1)
        
        Fizz = [x for x in nums if x%3 == 0]
        Buzz = [x for x in nums if x%5 == 0]
        FizzBuzz = [x for x in Fizz if x%5 == 0]
        
        r = map(str, nums)

        for i in Fizz:
            r[i-1] = "Fizz"
        
        for i in Buzz:
            r[i-1] = "Buzz"

        for i in FizzBuzz:
            r[i-1] = "FizzBuzz"
        
     
        return r
