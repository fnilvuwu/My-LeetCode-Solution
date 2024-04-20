class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ""
        for chars in zip(*strs):
            unique_char = ''.join(set(chars))
            if len(unique_char) == 1:
                common_prefix = common_prefix + unique_char
            else:
                break
        return common_prefix
