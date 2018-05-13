#784. Letter Case Permutation
'''
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.
'''
class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        if S.isdigit() or S == '':
            return [S]
        permutation = ['']

        for s in S:
            if s.isdigit():
                permutation = [ i+s for i in permutation]
            else:
                permutation = [ i+j for i in permutation for j in [s.lower(), s.upper()]]

        return permutation
            

