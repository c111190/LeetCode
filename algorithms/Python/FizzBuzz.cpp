/*
# 412. Fizz Buzz
# Write a program that outputs the string representation of numbers from 1 to n.
#
# But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. 
# For numbers which are multiples of both three and five output “FizzBuzz”.
#
*/

class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> r;
        for(int i=1; i<n+1; i++)
        {
            if( i%3 == 0){
                if( i%5 == 0){
                    r.push_back("FizzBuzz");
                }
                else
                    r.push_back("Fizz");
            }
            else if( i%5 == 0)
                r.push_back("Buzz");
            else
                r.push_back(to_string(i));
            
        }
        return r;
    }
};