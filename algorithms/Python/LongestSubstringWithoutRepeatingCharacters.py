'''
3. Longest Substring Without Repeating Characters
Given a string, find the length of the longest substring without repeating characters.
Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        used = {}
        start = maxlength = 0

        for i, c in enumerate(s):

            if c in used and start <= used[c]:
                start = used[c] + 1
                if maxlength > (len(s) - start):
                    return maxlength

            else:
                maxlength = max(maxlength, i - start + 1)

            used[c] = i

        return maxlength