#754. Reach a Number
'''
You are standing at position 0 on an infinite number line. There is a goal at position target.

On each move, you can either go left or right. During the n-th move (starting from 1), you take n steps.

Return the minimum number of steps required to reach the destination.
'''
class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target = abs(target)
        cum, i = 0, 0
        
        while target > cum or cum%2 != target%2:
            i+=1
            cum += i
            
        return i
