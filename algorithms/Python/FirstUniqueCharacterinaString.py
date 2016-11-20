'''
# 387. First Unique Character in a String
# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
# https://leetcode.com/problems/first-unique-character-in-a-string/
'''

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s) == 1:
            return 0

        t = s
        while(t != ""):
            if t.count(t[0]) == 1:
                return s.find(t[0])
            t = t.replace(t[0], "")
            
        return -1