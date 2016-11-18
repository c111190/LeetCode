/*
# 7.Reverse Integer
# Reverse digits of an integer.
#
# Example1: x = 123, return 321
# Example2: x = -123, return -321
#
*/

class Solution {
public:
    int reverse(int x) {
        
        int max, min;
        long long r = 0;
        max = 2147483647;
        min = -2147483647;
        
        while(abs(x) > 0){

            r = r * 10 + x % 10;
            x = x / 10;
        }
        if(r > max || r < min)
            r = 0;
          
        return r;
    }
};

