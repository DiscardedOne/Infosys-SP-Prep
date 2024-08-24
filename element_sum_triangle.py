n = int(input('Number of elements in array: '))
a=[]

for i in range(n):
    a.append(int(input('Element {}: '.format(i+1))))

tr=[]
tr.append(a)

while len(tr[-1])>1:
    temp=[]
    for i in range(len(tr[-1])-1):
        temp.append(tr[-1][i]+tr[-1][i+1])
    tr.append(temp)

tr.reverse()

print('The triangle is :-')

for i in tr:
    str_list = [str(item) for item in i]
    print(' '.join(str_list))









'''
Given an array form a triangle such that the last row of the triangle contains all the elements of the array and the row 
above it will contain the sum of two elements below it.
'''