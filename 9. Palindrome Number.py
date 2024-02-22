class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_rev = str(x)[::-1]
        if str(x) == x_rev:
            return True
        return False
        