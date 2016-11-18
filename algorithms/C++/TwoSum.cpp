/*
# 1.Two Sum
#
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution.
#
*/

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> r;
       
        int gap_max = target - *max_element(nums.begin(), nums.end());
        int gap_min = target - *min_element(nums.begin(), nums.end());
        
        for(int i=0; i<nums.size(); i++){
            if( nums[i] < gap_max || nums[i] > gap_min)
                continue;

            for(int j=nums.size()-1; j>i; j--){
                if(nums[i] + nums[j] == target)
                {
                    r.push_back(i);
                    r.push_back(j);
                    return r;
                }
            }
        }
        return r;
    }
};