n = int(input("Enter the total number of days: "))
m = int(input("Enter the total number of obligations: "))
k = int(input("Enter the largest number of obligations he can cancel: "))

d_m = list()
for i in range(m):
    d_m.append(int(input('Day {}: '.format(i+1))))

r=0
l=0
count=0
maxD=0
summ=0
d=[0]*n

for i in d_m:
    d[i-1]+=1

print('Schedule by Day: ',d)

for i in range(n):
    if count>maxD: maxD=count
    while summ+d[i]>k:
        summ=summ-d[l]
        l+=1
        count-=1
    r=i
    summ+=d[i]
    count+=1

print('Max Vacation Days are : ', maxD)

# for i in range(1,m):
#     # print('curr', d[i])
#     # print('prev', d[i-1])
#     if d[i]==d[i-1]+1 and count<=k:
#         if count==0: 
#             # print('one')
#             summ=d[i]+d[i-1]
#             count=2
#         else: 
#             # print('two')
#             summ+=d[i]
#             count+=1
#     else:
#         # print('three')
#         count=0
#         if summ>maxD: maxD=summ
#         summ=0

# if summ==0:
#     summ=d[0]

# print('Max Days of Vacation is:', maxD)


# for i in range(n):
#     if d[i]>k:
#         summ=0
#         if count>maxD: maxD=count
#         count=0
#         continue
#     elif d[i]<=k:
#         if summ==0:
#             l=i
#             r=i
#             summ+=d[i]
#             count+=1
#         elif summ+d[i]<=k:
#             r=i
#             summ+=d[i]
#             count+=1
#         elif summ+d[i]>k:
#             while summ+d[i]>k:
#                 summ=summ-d[l]
#                 l+=1
#                 count-=1
#             r=i
#             summ+=d[i]
#             count+=1
