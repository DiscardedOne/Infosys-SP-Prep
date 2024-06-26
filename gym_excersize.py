e = int(input('Energy: '))
n = int(input('Number of excersizes: '))
a=[]

for i in range(n):
    a.append(int(input('Energy cost of {}: '.format(i+1))))

a.sort(reverse=True)
count=0

for i in a:
    if e-(2*i)>=0:
        e-=2*i
        count+=2
    elif e-i>=0:
        e-=i
        count+=1
if e>0:
    print('The result is: ',-1)
else:
    print('The result is: ',count)