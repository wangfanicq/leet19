class Solution:
    def lengthOfLongestSubstring(self,s):
        if not s:
            return 0
        if len(s) == 1:
            return 1
        dic = {}
        start = 0
        length = 0
        for i in range(len(s)):
            if s[i] in dic:
                start = max(start,dic[s[i]]+1)
            dic[s[i]] = i
            length = max(length,i-start+1)
        return length
a = Solution()
print(a.lengthOfLongestSubstring('abcdade'))
