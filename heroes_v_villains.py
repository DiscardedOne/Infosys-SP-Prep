n = int(input('Number of villains: '))
m = int(input('Number of heroes: '))
h = int(input('Health of each hero: '))
v=[]

for i in range(n):
    v.append(int(input('Enter the health of villain {}: '.format(i+1))))


vCount=0
tvh=0
thh=h*m
hd=0

for i in range(n):
    if v[i]>h:
        v.pop(i)
        vCount+=1

for i in range(n):
    tvh+=v[i]

if tvh>thh:
    hd=tvh-thh

for i in range(n):
    if hd>0:
        hd-=v[i]
        vCount+=1
    elif hd<=0:
        break

print('{} villains must be removed'.format(vCount))