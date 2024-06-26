n = int(input('Number of characters in string: '))
s = input('The String: ')
cash = int(input('Max cash available: '))
a = int(input('Cost of swapping: '))
b = int(input('Cost of flipping: '))

if n<4:
    temp='0'*(4-n)
    s=temp.join(s)

def zeroesToFront(s, n):
    global cash
    l=list(s)
    index1=False
    for i in range(n):
        if index1==False and l[i]=='0':
            continue
        elif index1==False and l[i]=='1':
            index1=i
            for j in range(i+1, n):
                if l[j]=='0':
                    l[i], l[j] = l[j], l[i]
                    cash-=a
                    if cash<=0: return ''.join(l)
                    index1=False
                    break
            if not index1==False:
                break
    return ''.join(l)

def binaryToDecimal(s):
    summ=0
    power=n-1
    for i in s:
        summ+=int(i)*(2**power)
        power-=1
    return summ

if b>=a:
    rStr=zeroesToFront(s,n)
    lstr=list(rStr)

    for i in range(n):
        if lstr[i]=='1':
            cash-=b
            if cash<0: break
            lstr[i]='0'
    
    print('The least-ugly decimal value is: ',binaryToDecimal(''.join(lstr)))

elif b<a:
    cash2=cash
    rStr=zeroesToFront(s,n)
    lstr=list(rStr)

    for i in range(n):
        if lstr[i]=='1':
            cash-=b
            if cash<0: break
            lstr[i]='0'
    d1=binaryToDecimal(''.join(lstr))

    lstr2=list(s)
    for i in range(n):
        if lstr2[i]=='1':
            cash2-=b
            if cash2<0: break
            lstr2[i]='0'
    d2=binaryToDecimal(''.join(lstr2))

    print('The least-ugly decimal value is: ', d2 if d2<=d1 else d1)

