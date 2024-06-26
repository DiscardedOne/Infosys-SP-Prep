n = int(input('Enter the number of elements: '))
l = list()

for i in range(n):
    l.append(int(input('Element {}: '.format(i+1))))

count=0

if n%2==0:
    mid=n//2
    
    if not l[mid]==l[mid-1]:
        l[mid]=l[mid-1]
    for i in range(mid-1, 0, -1):
        if not l[i-1] == l[i]-1:
            count+=1
            l[i-1] = l[i]-1
    for i in range(mid+1,n,1):
        if not l[i] == l[i-1]-1:
            count+=1
            l[i] = l[i-1]-1
else:
    m1=(n//2)-1
    m2=(n//2)+1

    for i in range(m1,-1,-1):
        if not l[i]==l[i+1]-1:
            count+=1
            l[i]=l[i+1]-1
    for i in range(m2,n,1):
        if not l[i]==l[i-1]-1:
            count+=1
            l[i]=l[i-1]-1

print('Count is:',count, l)
    