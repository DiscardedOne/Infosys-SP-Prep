n = int(input('Enter the number of segments: '))
l = list()

for i in range(n):
    l.append(int(input('Height of segment {}: '.format(i+1))))

l.sort(reverse=True)

d=1
flag=True

while flag:
    red=2*d-1
    flag=False
    for i in range(1, n):
        if l[i]>=l[i-1]:
            l[i]=l[i]-red
            flag=True
    if flag==False:
        d-=1
        break
    l.sort(reverse=True)
    d+=1

print('It would take {} days.'.format(d))