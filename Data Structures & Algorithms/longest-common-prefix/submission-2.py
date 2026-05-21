class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=strs[0]
        if not strs:
            return ''
        for string in strs[1:]:
            i=0
            while i<len(string) and i<len(prefix) and prefix[i]==string[i]:
                i+=1
            prefix=prefix[:i]
            if not prefix:
                return ''
        return prefix 