m = int(input('Enter the decimal number: '))

def decimalToK_ary(m,k):
    d=[]
    q=m
    while q>0:
        d.append(q%k)
        q=q//k
    d.reverse()
    return d

res=0
for k in range(2,m):
    val = decimalToK_ary(m,k)
    if len(set(val))==1:
        res=k
        break
print('The result is:',res)