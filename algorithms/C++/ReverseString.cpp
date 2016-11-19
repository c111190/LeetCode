/*
# 344. Reverse String
#
# Write a function that takes a string as input and returns the string reversed.
# https://leetcode.com/problems/reverse-string/
#
*/

class Solution {
public:
    string reverseString(string s) {
        
        reverse(s.begin(), s.end());
        return s;
        
    }
};