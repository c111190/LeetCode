#50. Pow(x, n)
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        if n == 0:
            return 1
        elif n == 1:
            return x
        
        else:
            
            if n < 0:
                x = 1/x
                n = abs(n)
            mypow = x
                
            while n > 1:
                if n%2 != 0:
                    mypow *= x
                mypow *= x
                x *= x
                n = math.floor(n/2)
               
        return mypow
