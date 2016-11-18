'''
: 6. ZigZag Conversion
: https://leetcode.com/problems/zigzag-conversion/
:
'''

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        if numRows == 1:
            return s
            
        r = ""
       
        multilist = ["" for row in range(numRows)]
        
        for idx, x in enumerate(s):
            
            i = idx%(numRows*2-2)
            if i > numRows-1:
                i = (numRows-1)*2 - i
            
            multilist[i] = multilist[i] + x
        
        for list in multilist:
            r = r + list
        return r