n = int(input('Enter the number of Monsters: '))
e = int(input('Enter the initial experience points: '))
p = []
b = []
a = []
count=0

for i in range(n):
    p.append(int(input('Power of Monster {}: '.format(i+1))))
for i in range(n):
    b.append(int(input('Bonus of Monster {}: '.format(i+1))))
for i in range(n):
    a.append([p[i],b[i]])

a.sort()

for m in a:
    if e<m[0]:
        break
    e+=m[1]
    count+=1

print('{} Monsters Defeated!'.format(count))
