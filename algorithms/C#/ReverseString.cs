/*
# 344. Reverse String
#
# Write a function that takes a string as input and returns the string reversed.
# https://leetcode.com/problems/reverse-string/
#
*/

public class Solution {
    public string ReverseString(string s) {
        
        return new string (s.Reverse().ToArray());
    }
}