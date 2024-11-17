class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        openBracket = ['(','{','[']
        closeBracket = [')','}',']']

        if len(s) < 2:
            return False

        for i in s:
            if i in openBracket:
                stack.append(i)
            elif i in closeBracket:
                if len(stack) == 0:
                    return False
                elif openBracket[closeBracket.index(i)] == stack[-1]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0