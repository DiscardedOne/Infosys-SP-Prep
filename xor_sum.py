n = int(input('Number of elements in A: '))
k = int(input('Max value of x: '))
a=[]

for i in range(n):
    a.append(int(input('Element {}: '.format(i+1))))

maxx=0

for i in range(0,k+1):
    xs=0
    for j in range(n):
        xs+=(i^a[j])
    if xs>maxx: 
        maxx=xs

print('The max value of xor_sum is:', maxx)