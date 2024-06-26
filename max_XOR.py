n = int(input('Number of elements: '))
l=[]

for i in range(n):
    l.append(int(input('Element {}: '.format(i+1))))

l.sort(reverse=True)

l=l[:n//2]

maxx=l[0]
xor=l[0]

for i in range(1,len(l)):
    xor^=i
    if maxx<xor:
        maxx=xor

print('The max xor value is: ',maxx)