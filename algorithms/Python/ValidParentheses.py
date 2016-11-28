'''
# 20. Valid Parentheses
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
# https://leetcode.com/problems/valid-parentheses/
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        right = ")]}"
        left = "([{"
        stack = []
        
        ff = [t for t in s if t in "(){}[]"]
        
        
        for token in ff:
            if token in left:
                stack.append(token)
                continue
                
            elif token in right:
                try:
                    if left[right.index(token)] == stack[-1]:
                        stack = stack[:-1]
                    else:
                        return False
                except:
                    return False
                
        if len(stack) != 0:
            return False
            
        return True