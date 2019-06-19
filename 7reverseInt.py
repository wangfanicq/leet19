class Solution:
    def reverseInt(self,x):
        if not x:
            return 0
        strx=str(x)
        tmp=strx[::-1].lstrip('0').rstrip('-')
        add='-' if strx[0]=='-' else ''
        res=int(add+tmp)
        if res>=2**31 or res<-2**31:
            return 0
        else:
            return res
a=Solution()
b=int(input())
print(a.reverseInt(b))
'''
#following way2 not using string
class Solution:
    def reverseInt(self,x):
        if not x:
            return True
        if x<0 or x%10==0:
            return False
        tmp=0
        while x>tmp:
            tmp=tmp*10+x%10
            x//=10
        return x==tmp or x==tmp//10
'''
