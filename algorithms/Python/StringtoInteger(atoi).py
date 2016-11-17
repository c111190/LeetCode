class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        r = 0
        i = 0
        sign = 1
        
        str = str.strip()
        if len(str) > 0:
            if ord(str[0]) == 45: # '-'
                sign = -1
                i = 1
            elif ord(str[0]) == 43: # '+'
                i = 1

            for idx in range(i, len(str)):
                num_ascii = ord(str[idx]) - 48 
                if (num_ascii >= 0) and (num_ascii <= 9):
                    r = r*10 + num_ascii
                else:
                    break;
            r = r*sign
            
            # check the limit of integer
            if r > 2147483647:
                r = 2147483647
            elif r < -2147483648:
                r = -2147483648
        return r