class ListNode():
    def __init__(self,x):
        self.val = x
        self.next = None
class Solution():
    def addTwoNumbers(self,l1,l2):
        if not l1 and not l2:
            return 0
        #first instance a dummy node to begin
        dummy = ListNode(0)
        cur = dummy
        tmp = 0
        add = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            tmp = (x+y+add)%10
            add = (x+y+add)//10
            cur.next = ListNode(tmp)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            cur = cur.next
        if add > 0:
            cur.next = ListNode(add)
        return dummy.next
c=ListNode(2)
d=ListNode(3)
e=ListNode(6)
c.next=d
d.next=e
f=ListNode(9)
g=ListNode(5)
f.next=g
a=Solution()
res=a.addTwoNumbers(c,f)
t=[]
while res:
    t.append(res.val)
    res=res.next
print(t)

