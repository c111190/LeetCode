#806. Number of Lines To Write String
'''
We are to write the letters of a given string S, from left to right into lines. Each line has maximum width 100 units, and if writing a letter would cause the width of the line to exceed 100 units, it is written on the next line. We are given an array widths, an array where widths[0] is the width of 'a', widths[1] is the width of 'b', ..., and widths[25] is the width of 'z'.

Now answer two questions: how many lines have at least one character from S, and what is the width used by the last such line? Return your answer as an integer list of length 2.
'''
class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        
        w, line = 0, 0
        for s in S:
            w += widths[ord(s)-97]
            if w > 100:
                line += 1
                w = widths[ord(s)-97]
                
        if w != 0:
            line += 1
        return [line, w]
