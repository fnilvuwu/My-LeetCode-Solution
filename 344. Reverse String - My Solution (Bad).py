class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left_pointer= 0

        right_pointer= len(s) - 1
        for i in range(0, right_pointer):
            left_pointer += 1            
            right_pointer -= 1
            s.append(s[right_pointer])
        for i in range(0, left_pointer):
            del s[0]