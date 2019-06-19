class Solution:
    def isPalindrome(self, x: int) -> bool:
        if not x:
            return True
        if x<0 or x%10==0:
            return False
        #follow not use string space
        tmp=0
        while x>tmp:
            tmp=tmp*10+x%10
            x//=10
        return tmp==x or x==tmp//10
        '''strx=str(x)
        return strx==strx[::-1]'''

