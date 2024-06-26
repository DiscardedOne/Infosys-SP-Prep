from collections import Counter

s = input('Enter the string: ')
ratio={}

sl = Counter(s)

sortedData= sorted(sl.items(), key=lambda x: x[1])

print(sortedData[0][1])