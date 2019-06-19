class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ''
        if len(strs)==1:
            return strs[0]
        prefix=strs[0]
        for i in range(1,len(strs)):
            while strs[i].find(prefix)!=0:
                prefix=prefix[:-1]
                if not prefix:
                    return ''
        return prefix
#way2 use zip
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ''
        if len(strs)==1:
            return strs[0]
        zipa=zip(*strs)
        res=''
        for i in zip:
            if len(set(i))==1:
                res+=i[0]
            else:
                break
        return res
#way3 compare every column
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ''
        if len(strs)==1:
            return strs[0]
        prefix=strs[0]
        res=''
        for i in range(len(prefix)):
            for j in range(1,len(strs)):
                while len(strs[j]==i or strs[j][i]!=prefix[i]:
                    return res
            res+=prefix[i]
        return res


