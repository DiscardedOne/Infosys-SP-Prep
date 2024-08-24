rows = int(input('Number of rows in grid: '))
cols=2
grid=[]

for row in range(rows):
    col_input=[int(val) for val in input(f'Enter values in row {row+1}: ').strip().split(' ')]
    if len(col_input)==1: col_input.append(0)
    grid.append(col_input)

path=[]
total_value=0
prev_val=0
for row in range(rows):
    if grid[row][0]>=grid[row][1] and grid[row][0]>prev_val:
        path.append([row+1,0+1])
        total_value+=grid[row][0]
        prev_val=grid[row][0]
    elif grid[row][1]>prev_val:
        path.append([row+1,1+1])
        total_value+=grid[row][1]
        prev_val=grid[row][1]

print('The maximum value is: ',total_value)
print('For the path: ', path)







'''
Grid Path
Given a grid. Each cell of the grid contains a single integer value. These values are described by 2D 
integer array a with N rows and 2 columns, where a[i][j] is the value in the cell located in row i, 
column j.
Standing in (i; j), the player can move to any cell of the next row (i+1; j2) under the condition that 
a[i+1][j2] > a[i][j]. In other words, the value in the next cell of the player's path should be strictly 
greater than the value in the current cell of the player's path.
The player can't make any moves if he's already in the last row.
If the player starts in any cell of the first row (either (1; 1) or (1; 2)), what is the maximum possible 
total sum of values in all cells he can visit on his path?
Print the answer modulo 10^9+7.

Input:
The first line contains an integer, n, denoting the number of rows in a.
The next line contains an integer, 2, denoting the number of columns in a.
Each line i of the n subsequent lines (where 0 ≤ i < n) contains 2 space separated integers each 
describing the row a[i]. 

Sample cases:

Input 
2
1 2 
3 4 

Output
6 

Output description
Optimal path is (1;2)->(2;2). 
The answer is 2+4=6.

Input
2
7 8 
5 5 

Output
8 

Output description
No moves are possible from the first row. So start in (1; 2) and 
collect just 8.

Input
3
1 1 
2 2 
3 3

Output
6 

Output description
One of the optimal paths is (1;1)->(2;1)->(3;1). 
The answer is 1+2+3=6
'''