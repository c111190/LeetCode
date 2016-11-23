/*
# 9. Palindrome Number
# Determine whether an integer is a palindrome. Do this without extra space.
#
# https://leetcode.com/problems/palindrome-number/
*/

public class Solution {
    public bool IsPalindrome(int x) {
        
        if( x < 0 )
            return false;
            
        string num = Convert.ToString(x);
        int max_loc = num.Length-1;
        int mid_loc = (int) num.Length/2;
        
        for(int i=0; i<mid_loc; i++){
            if(num[i] != num[max_loc-i])
                return false;
        }
        return true;
    }
}