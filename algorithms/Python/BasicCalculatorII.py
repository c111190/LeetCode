#227. Basic Calculator II
'''
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.
'''

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        t = 0
        nums = []
        notation = "+"
        
        if s.isdigit():
            return int(s)
        s = s.strip()
        
        for i in xrange(len(s)):
            if not s[i] == " ":
                if s[i].isdigit():
                    t = t*10+int(s[i])
                    
                if (not s[i].isdigit()) or (i == len(s)-1):
                    
                    if notation == "+":
                        nums.append(t)
                    elif notation == "-":
                        nums.append(-t)
                    elif notation == "*":
                        nums.append(nums.pop()*t)
                    else:
                        b = nums.pop()
                        n = b/abs(b) if b != 0 else 0
                        nums.append(int(abs(b)/t*n))
                    
                    notation = s[i]
                    t = 0

        return sum(nums)
